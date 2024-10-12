from . import ServerPacket

class QuestionEndPacket(ServerPacket):
    def __init__(self, data: dict):
        super().__init__(data)
        self.rank = self.content['rank']
        self.total_score = self.content['totalScore']
        self.is_correct = self.content['isCorrect']
        self.correct_choices = self.content['correctChoices']
