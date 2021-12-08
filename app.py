from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/fixtures')
def fixtures_page():
    games = [
        {'id': 1, 'home_team': 'Man City', 'away_team': 'Everton', 'H': '70%','D': '20%', 'A':'10%'},
        {'id': 2, 'home_team': 'Chelsea', 'away_team': 'Liverpool', 'H': '65%', 'D': '25%', 'A': '10%'},
        {'id': 3, 'home_team': 'Stoke City', 'away_team': 'Man Utd', 'H': '25%', 'D': '30%', 'A':'55%'}
    ]
    return render_template('fixtures.html', games=games)

@app.route('/tables')
def table_page():
    return render_template('tables.html')

@app.route('/about')
def about_page():
    return render_template('about.html')