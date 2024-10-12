from . import ServerPacket

class QuestionReadyPacket(ServerPacket):
    def __init__(self, data: dict):
        super().__init__(data)
        self.game_block_index = self.content['gameBlockIndex']
        self.total_game_block_count = self.content['totalGameBlockCount']
        self.time_available = self.content['timeAvailable']
        self.number_of_choices = self.content['numberOfChoices']
        self.question_index = self.content['questionIndex']
