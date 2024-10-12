import asyncio
from kahoot import KahootClient
from kahoot.packets.impl.respond import RespondPacket
from kahoot.packets.server.game_over import GameOverPacket
from kahoot.packets.server.game_start import GameStartPacket
from kahoot.packets.server.question_end import QuestionEndPacket
from kahoot.packets.server.question_ready import QuestionReadyPacket
from kahoot.packets.server.question_start import QuestionStartPacket

client: KahootClient = KahootClient()

async def game_start(packet: GameStartPacket):
    print(f"Game started: {packet}")

async def game_over(packet: GameOverPacket):
    print(f"Game over: {packet}")

async def question_start(packet: QuestionStartPacket):
    print(f"Question started: {packet}")
    await client.send_packet(RespondPacket(client.game_pin, 1, 1))

async def question_end(packet: QuestionEndPacket):
    print(f"Question ended: {packet}")

async def question_ready(packet: QuestionReadyPacket):
    print(f"Question ready: {packet}")

async def main():
    game_pin: int = int(input("Enter the game pin: "))
    name: str = input("Enter your name: ")

    # Register event handlers before joining the game
    client.on("game_start", game_start)
    client.on("game_over", game_over)
    client.on("question_start", question_start)
    client.on("question_end", question_end)
    client.on("question_ready", question_ready)

    # Join the game
    await client.join_game(game_pin, name)

if __name__ == "__main__":
    asyncio.run(main())