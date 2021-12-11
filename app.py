from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    homeTeam = db.Column(db.String(), nullable=False)
    awayTeam = db.Column(db.String(), nullable=False)
    homeProb = db.Column(db.String(), nullable=False)
    drawProb = db.Column(db.String(), nullable=False)
    awayProb = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Game {self.homeTeam}'


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/fixtures')
def fixtures_page():
    games = Game.query.all()
    return render_template('fixtures.html', games=games)

@app.route('/tables')
def table_page():
    return render_template('tables.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')