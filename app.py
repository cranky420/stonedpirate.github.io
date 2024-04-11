import flask
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Global variable to store the count of visits
visits_count = 0

@app.route('/')
def index():
    global visits_count
    visits_count += 1
    return render_template('index.html', visits_count=visits_count)

@app.route('/play', methods=['POST'])
def play():
    global visits_count
    secret_number = random.randint(1, 100)
    guess = int(request.form['guess'])
    if guess == 69:  # Check if the guessed number is 69
        result = "Cheater! You used the cheat code! Congratulations!"
    elif guess < secret_number:
        result = "Too low! Try again."
    elif guess > secret_number:
        result = "Too high! Try again."
    else:
        result = f"Congratulations! You're a true Genius, you guessed the secret number {secret_number}!"
    return render_template('result.html', result=result, visits_count=visits_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
