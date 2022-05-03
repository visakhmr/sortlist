import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    file = open('teams.txt', 'r')
    teams = file.readlines()
    file = open('seed.txt', 'r')
    seed = file.readlines()[0]

    teams.sort()

    random.Random(seed).shuffle(teams)

    return render_template('index.html', teams=teams)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
