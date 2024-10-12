from logging import getLogger, StreamHandler, Formatter, DEBUG, CRITICAL

logger = getLogger("kahootpy")
handler = StreamHandler()
handler.setFormatter(Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

# Mute the logger by default
logger.setLevel(CRITICAL)
handler.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

def unmute_logger():
    """Unmute the logger to allow debug messages."""
    logger.setLevel(DEBUG)

def mute_logger():
    """Mute the logger to only show critical messages."""
    logger.setLevel(CRITICAL)
