function checkGuess() {
    var secretNumber = Math.floor(Math.random() * 100) + 1;
    var guess = parseInt(document.getElementById("guess").value);

    var messageElement = document.getElementById("message");

    if (isNaN(guess) || guess < 1 || guess > 100) {
        messageElement.textContent = "Please enter a valid number between 1 and 100.";
        return;
    }

    if (guess < secretNumber) {
        messageElement.textContent = "Too low! Try again.";
    } else if (guess > secretNumber) {
        messageElement.textContent = "Too high! Try again.";
    } else {
        messageElement.textContent = "Congratulations! You guessed the number " + secretNumber + "!";
    }
}
