from main import db

class Game(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    homeTeam = db.Column(db.String(), nullable=False)
    awayTeam = db.Column(db.String(), nullable=False)
    homeProb = db.Column(db.String(), nullable=False)
    drawProb = db.Column(db.String(), nullable=False)
    awayProb = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Game {self.homeTeam}'
