from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    runs_fingers = {
        1: "Index Finger",
        2: "Middle Finger",
        3: "Ring Finger",
        4: "Little Finger",
        5: "Thumb",
        6: "No Finger",
    }

    user_runs = int(request.form['runs'])

    comp_runs = random.randint(1, 6)

    user_finger = runs_fingers[user_runs]
    comp_finger = runs_fingers[comp_runs]

    result = ''
    if user_runs > comp_runs:
        result = "You won!"
    elif user_runs < comp_runs:
        result = "You lost!"
    else:
        result = "It's a tie!"

    return render_template('result.html', user_finger=user_finger, comp_finger=comp_finger, result=result)

if __name__ == '__main__':
    app.run(debug=True)
