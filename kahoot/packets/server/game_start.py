from . import ServerPacket


class GameStartPacket(ServerPacket):
    ID: int = 9

    def __init__(self, data: dict):
        super().__init__(data)
        self.game_block_count = self.content["gameBlockCount"]
        self.extensive_mode = self.content["extensiveMode"]
        self.kahoot_lang_is_rtl = self.content["kahootLangIsRTL"]
        self.upcoming_game_block_data = self.content["upcomingGameBlockData"]
