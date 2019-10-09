import random
import json
import datetime

current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 100)
attempts = 0

score_data = {"attempts": attempts, "date": datetime.datetime.now()}

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top score: " + str(score_list))

for score_dict in score_list:
    print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("Congratulations! You guessed the secret number, it's " + str(secret) +"!")
        print("Attempts needed: " + str(attempts))
        break
    elif guess < secret:
        print("That is not correct. The secret number is bigger.")
    elif guess > secret:
        print ("That is not correct. The secret number is smaller.")