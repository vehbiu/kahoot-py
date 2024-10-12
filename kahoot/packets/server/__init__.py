# packets/server/__init__.py
from dataclasses import dataclass
from typing import Optional, Any
from json import loads

@dataclass
class ServerPacket:
    gameid: Optional[int]
    id: Optional[int]
    type: str
    content: Any
    host: Optional[str] = None
    cid: Optional[str] = None

    def __init__(self, data: dict):
        self.gameid = data.get('gameid')
        self.id = data.get('id')
        self.type = data['type']
        self.content = data.get('content')
        if isinstance(self.content, str):
            try:
                self.content = loads(self.content)
            except Exception:
                pass
        self.host = data.get('host')
        self.cid = data.get('cid')

