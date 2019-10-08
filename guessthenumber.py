secret = 41


for x in range(5):
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == secret:
        print("Congratulations! You guessed the secret number!")
        break
    else:
        print("Sorry," + str(guess) + " is not the secret number!")