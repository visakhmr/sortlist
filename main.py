import random
from flask import Flask, render_template

app = Flask(__name__)

def sort_teams(teams_file, seed_file):
    file = open(teams_file, 'r')
    teams = file.readlines()
    file = open(seed_file, 'r')
    seed = file.readlines()[0]
    teams.sort()
    random.Random(seed).shuffle(teams)
    return teams

@app.route('/')
def root():
    teams1 = sort_teams('teams.txt', 'seed.txt')
    teams2 = sort_teams('secondary_projects.txt', 'seed.txt')
    teams3 = sort_teams('tertiary_projects.txt', 'seed.txt')

    return render_template('index.html', teams1=teams1, teams2=teams2, teams3=teams3)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
