import random

secret = random.randint(1, 100)
attempts = 0

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score (attempts): " + str(best_score))

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1

    if guess == secret:
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))

        print("Congratulations! You guessed the secret number, it's " + str(secret) +"!")
        print("Attempts needed: " + str(attempts))
        break
    elif guess < secret:
        print("That is not correct. The secret number is bigger.")
    elif guess > secret:
        print ("That is not correct. The secret number is smaller.")