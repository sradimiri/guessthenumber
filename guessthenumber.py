secret = 41


while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == secret:
        print("Congratulations! You guessed the secret number!")
        break
    else:
        print("Sorry," + str(guess) + " is not the secret number!")