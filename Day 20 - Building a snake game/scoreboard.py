from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.write(f'Score: {self.current_score}', align='center', font=['Arial', 8, 'normal'])
    
    def keep_score(self):
        self.current_score += 1

