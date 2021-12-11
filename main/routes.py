from main import app
from flask import render_template
from main.models import Game

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