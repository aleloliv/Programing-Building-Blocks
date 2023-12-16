import random
import time

print("Welcome to the number guessing game!")
print("In this game, you will guess a randomly generated number within a given range.")
print("Your score is calculated based on the number of attempts it takes you to guess the number.")
print("The fewer attempts it takes, the higher your score!")

while True:
    try:
        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))
        if min_num >= max_num:
            print("Invalid range. Please enter a minimum number that is less than the maximum number.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    difficulty = input("Select a difficulty level (easy, medium, hard): ").lower()
    if difficulty in ['easy', 'medium', 'hard']:
        break
    else:
        print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")

if difficulty == 'easy':
    max_attempts = 15
elif difficulty == 'medium':
    max_attempts = 10
else:
    max_attempts = 5

game = True
score = 0

while game:
    number = random.randint(min_num, max_num)

    if input("Show debug info? (yes or no)").lower() == 'yes':
        print(f"DEBUG: The number is {number}.")

    guess = 0
    count = 1

    while guess != number and count <= max_attempts:
        guess = input(f"What is your guess? ({min_num}-{max_num}) ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess < min_num or guess > max_num:
            print(f"Your guess should be between {min_num} and {max_num}")
            continue

        if guess > number:
            print("Lower")
        elif guess < number:
            print("Higher")
        else:
            print("You guessed it!.")
            time.sleep(1)
            print(f"You guessed the number in {count} attempt{'s' if count > 1 else ''}!")
            score += 100 - count * 10
            print(f"Your current score is {score}")
            break

        count += 1

    if count > max_attempts:
        print(f"You've used all {max_attempts} attempts. The number was {number}.")

    while True:
        selection = input("Do you want to show the leaderboard, play again, or quit? (leaderboard/play/quit) ").lower()
        if selection == "leaderboard":
            with open("leaderboard.txt", "r") as f:
                print("Leaderboard:")
                for i, line in enumerate(f):
                    print(f"{i+1}. {line.strip()}")
        elif selection == "play":
            break
        elif selection == "quit":
            game = False
            break
        else:
            print("Invalid input. Please enter 'leaderboard', 'play', or 'quit'.")

    with open("leaderboard.txt", "a+") as f:
        f.seek(0)
        scores = f.readlines()
        scores = [int(score.strip()) for score in scores]
        scores.append(score)
        scores.sort(reverse=True)
        scores = scores[:5]
        f.seek(0)
        f.truncate()
        for score in scores:
            f.write(f"{score}\n")

print("Thanks for playing!")
