import random

secret = random.randint(1, 100)
attempts = 0


while True:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1

    if guess == secret:
        print("Congratulations! You guessed the secret number, it's " + str(secret) +"!")
        print("Attempts needed: " + str(attempts))
        break
    elif guess < secret:
        print("That is not correct. The secret number is bigger.")
    elif guess > secret:
        print ("That is not correct. The secret number is smaller.")