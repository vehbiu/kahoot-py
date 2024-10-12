from .client import KahootClient
from .exceptions import KahootError, GameNotFoundError

__version__ = "0.1.0"
__all__ = ["KahootClient", "KahootError", "GameNotFoundError"]

async def join_game(game_pin: int, username: str) -> KahootClient:
    client = KahootClient()
    await client.join_game(game_pin, username)
    return client
