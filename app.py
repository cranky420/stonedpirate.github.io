import flask
from flask import Flask, render_template, request, redirect
import random

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')

# Global variable to store the count of visits
visits_count = 0

# Global variable to store the secret number for the guessing game
secret_number = None

@app.route('/')
def index():
    global visits_count
    visits_count += 1
    return render_template('questions.html', visits_count=visits_count)

@app.route('/questions', methods=['GET'])
def questions():
    global visits_count
    visits_count += 1
    return render_template('response.html', visits_count=visits_count)

@app.route('/play', methods=['POST', 'GET'])
def play():
    global visits_count
    global secret_number

    if request.method == 'POST':
        answer = request.form.get('answer')
        # Check if the answer is valid
        if answer in ['love', 'money', 'adventure', 'sex', 'dreams', 'sleep']:
            # Define responses based on the selected answer
            responses = {
                'love': "Great choice! Love is indeed important, but isn't there more to life?",
                'money': "Money can buy many things, but is everything buyable?",
                'adventure': "Adventure can bring excitement and fulfillment, but is it the essence of life?",
                'sex': "Dear Lusty friend. Physical intimacy is a part of life, but is it the ultimate purpose?",
                'dreams': "Dreams inspire us to strive for more, but are they the reality of life?",
                'sleep': "Sleep is essential for rest and rejuvenation, but is life just about sleeping?"
            }
            # Get the response based on the selected answer
            response = responses[answer]
            
            # Generate a secret number for the guessing game
            secret_number = str(random.randint(1, 100))

            # Render the response page with the response
            return render_template('index.html', response=response, visits_count=visits_count)
        else:
            # Invalid choice, redirect to questions page
            return redirect('/questions')
    else:
        # Redirect to the questions page if it's not a POST request
        return redirect('/questions')


@app.route('/guess', methods=['POST'])
def guess():
    global visits_count
    global secret_number

    # Ensure secret_number is set
    if secret_number is None:
        # Redirect to questions page if secret number is not generated
        return redirect('/questions')

    # Get guess from form
    guess_str = request.form.get('guess')

    # Ensure guess is not empty
    if not guess_str:
        return "Invalid guess"

    # Convert guess to integer
    guess = int(guess_str)

    # Check if the guess is correct
    if guess == 69:
        result = f"Bloody Cheater! didn't you knew the cheatcode?"
    elif guess == int(secret_number):
        result = f"You're the Chosen One. Congratulations! You guessed the secret number. {secret_number}!"
    elif guess < int(secret_number):
        result = "Soryy to say this, but you're fucking unlucky! Wanna try again?."
    else:
        result = "Fuck is Fuck. There's nothing as more Fuck or less Fuck! Wanna try again?."

    # Render the result page
    return render_template('result.html', result=result, visits_count=visits_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
