from dataclasses import dataclass
from typing import Optional
from json import dumps

@dataclass
class Packet:
    id: Optional[int]
    type: str
    gameid: int
    content: dict
    host: str = "kahoot.it"

    def to_dict(self):
        out: dict = self.__dict__.copy()

        if self.id is None:
            out.pop("id")

        if isinstance(self.content, dict):
            out["content"] = dumps(self.content)

        return out

