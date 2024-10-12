from .. import Packet
from ...constants import USER_AGENT

class LoginPacket(Packet):
    name: str

    def __init__(self, gameid: int, name: str):
        self.name = name
        super().__init__(
            id=None,
            type="login",
            gameid=gameid,
            content={
                "device": {
                    "userAgent": USER_AGENT,
                    "screen": {"width": 1920, "height": 1080}
                }
            }            
        )
