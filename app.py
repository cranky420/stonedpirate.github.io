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
    if guess == 69:  # Check if the guessed number is 69
        result = "প্রতারক ! আপনি চিট কোড ব্যবহার করেছেন! অভিনন্দন!"
        # Cheater! You used the cheat code! Congratulations!
    elif guess < secret_number:
        result = "অনেক কম! আবার চেষ্টা কর."
        # Too low! Try again.
    elif guess > secret_number:
        result = "খুব উচ্চ! আবার চেষ্টা কর."
        # Too high! Try again.
    else:
        result = f"Congratulations! You're a true Genius, you guessed the seceret number {secret_number}!"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=False)
