from .. import Packet


class RespondPacket(Packet):
    # id: int = 12

    def __init__(self, gameid: int, choice: int, question_index: int):
        super().__init__(
            id=None,
            type="message",
            gameid=gameid,
            content={"type": "quiz", "choice": choice, "questionIndex": question_index},
        )
        self.id = 45
