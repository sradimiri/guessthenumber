secret = "41"

guess = input("Guess the number between 1 and 100: ")

if guess == secret:
    print("Congratulations! You guessed the secret number!")
else:
    print("Sorry," + str(guess) + " is not the secret number!")