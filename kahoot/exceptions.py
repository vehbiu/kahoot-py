class KahootError(Exception):
    """Base exception for Kahoot client"""
    pass

class GameNotFoundError(KahootError):
    """Raised when a game with the specified pin is not found"""
    pass