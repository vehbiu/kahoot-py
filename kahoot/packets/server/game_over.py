from . import ServerPacket

class GameOverPacket(ServerPacket):
    def __init__(self, data: dict):
        super().__init__(data)
        self.rank = self.content['rank']
        self.quiz_title = self.content['quizTitle']
        self.quiz_id = self.content['quizId']
        self.correct_count = self.content['correctCount']
        self.incorrect_count = self.content['incorrectCount']
        self.total_score = self.content['totalScore']
