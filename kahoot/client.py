import re
import time
import json
import httpx
import aiocometd_noloop as aiocometd

from kahootpy.packets.server import ServerPacket
from typing import Tuple, Dict

from .packets import Packet
from .packets.impl.login import LoginPacket
from .util.solver import solve_challenge
from .exceptions import GameNotFoundError
from .util.logger import logger
from .constants import USER_AGENT

class KahootClient:
    def __init__(self):
        self.http_client = httpx.Client(
            headers={"User-Agent": USER_AGENT}
        )
        self.game_pin: int = None
        self.event_handlers: Dict[str, list[callable]] = {}
        self.client: aiocometd.Client = None

    def on(self, event: str, handler):
        """Register an event handler."""
        if event not in self.event_handlers:
            self.event_handlers[event] = []
        self.event_handlers[event].append(handler)

    async def game_exists(self, pin: int) -> bool:
        try:
            r = self.http_client.get(
                f"https://kahoot.it/reserve/session/{pin}/?{int(time.time())}"
            )
            return r.status_code != 404
        except Exception:
            return False

    async def send_packet(self, packet: Packet):
        await self._emit_message('/service/controller', packet)    
    
    async def _emit_message(self, channel: str, data: Packet | dict):
        if isinstance(data, Packet):
            data = data.to_dict()
        await self.client.publish(channel, data)

    async def join_game(self, game_pin: int, username: str):
        logger.info(f"Joining game {game_pin} as {username}")
        try:
            r = self.http_client.get(
                f"https://kahoot.it/reserve/session/{game_pin}/?{int(time.time())}"
            )
            logger.debug(f"Game exists: {r.status_code != 404}")
            if r.text == "Not found":
                raise GameNotFoundError(f"Game with pin {game_pin} not found")
            
            session_token = r.headers['x-kahoot-session-token']
            logger.debug(f"Session token: {session_token}, Solving challenge...")
            session_id = solve_challenge(session_token, r.json()["challenge"])
            logger.debug(f"Session ID: {session_id}")

            self.game_pin = game_pin
            
            await self._establish_connection(session_id, username)

        except GameNotFoundError:
            raise
        except Exception as e:
            logger.error(f"Error joining game: {e}")

    async def _establish_connection(self, session_id: str, username: str):
        self.client = aiocometd.Client(f"wss://play.kahoot.it/cometd/{self.game_pin}/{session_id}", ssl=True)
        await self.client.open()
        await self._setup_subscriptions(self.client)
        await self._send_login_message(self.game_pin, username)
        logger.debug("Connection established")

        async for raw_message in self.client:
            message = raw_message['data']
            await self._handle_message(self.game_pin, message)
            logger.debug("[Server->Client] " + str(message))

        await self.client.close()

    async def _setup_subscriptions(self, client):
        await client.subscribe("/service/controller")
        await client.subscribe("/service/player")
        await client.subscribe("/service/status")

    async def _send_login_message(self, game_pin: int, username: str):
        await self._emit_message('/service/controller', LoginPacket(game_pin, username))

    def _parse_packet(self, message: Packet) -> Packet:
        # packet_classes = [GameStartPacket, QuestionReadyPacket, QuestionStartPacket, QuestionEndPacket, GameOverPacket]
        packet_classes: Tuple[Packet] = ServerPacket.__subclasses__()
        for packet_class in packet_classes:
            try:
                return packet_class(message)
            except Exception:
                pass
        return None

    async def _handle_message(self, game_pin: int, message: dict):
        message_type = message.get('type')
        packet = self._parse_packet(message)


        if packet:
            event_name: str = packet.__class__.__name__.split("Packet")[0]
            event_name = re.sub(r'(?<!^)(?=[A-Z])', '_', event_name).lower()

            await self._trigger_event(event_name, packet)
            logger.debug(f"Received packet: {packet}")
       
        
        if message_type == "question":
            await self._trigger_event("question", message)
        elif message_type == "status" and message.get("status") == "ACTIVE":
            await self._trigger_event("connect", message)
        elif message_type == "loginResponse":
            await self._handle_login_response(game_pin)

    async def _trigger_event(self, event: str, data: any):
        """Trigger registered event handlers."""
        if event in self.event_handlers:
            for handler in self.event_handlers[event]:
                await handler(data)

    async def _handle_login_response(self, game_pin: int):
        await self.client.publish('/service/controller', {
            "id": 16,
            "type": "message",
            "host": "kahoot.it",
            "gameid": game_pin,
            "content": json.dumps({"usingNamerator": False})
        })
