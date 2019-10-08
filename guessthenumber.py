secret = 41


while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == secret:
        print("Congratulations! You guessed the secret number!")
        break
    elif guess < secret:
        print("That is not correct. The secret number is bigger.")
    elif guess > secret:
        print ("That is not correct. The secret number is smaller.")