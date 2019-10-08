secret = 41
guess = 0

while guess != secret:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == secret:
        print("Congratulations! You guessed the secret number!")
    else:
        print("Sorry," + str(guess) + " is not the secret number!")