import flask
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    secret_number = random.randint(1, 100)
    guess = int(request.form['guess'])
    if guess < secret_number:
        result = "Too low! Try again."
    elif guess > secret_number:
        result = "Too high! Try again."
    elif guess == 69:
        result = "Hurray!! you hit the JACKPOT"
    else:
        result = f"Congratulations! You guessed the number {secret_number}!"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=False)
