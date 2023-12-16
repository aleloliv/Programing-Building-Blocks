#implemented a list of words that the games randomly picks from, added a while loop to continue the game if the player desires to, added a limit on the number of attempts. Defined a function to return the hint following the rules

import random  # imports the random library

def get_hint(word, guess):  # defines a function to generate the hint based on user's guess and the secret word
    hint = ["_" for _ in word]  # initializes a hint list with underscores having the same length as the secret word
    for i, letter_g in enumerate(guess):  # loops through each letter of the user's guess, using enumerate() to access the index
        if letter_g.lower() in word.lower():  # checks if the letter is in the secret word, regardless of case
            if letter_g.lower() == word[i].lower():  # checks if the letter is in the correct position
                hint[i] = letter_g.upper()  # replaces the underscore with the correct letter in uppercase
            else:
                hint[i] = letter_g.lower()  # replaces the underscore with the correct letter in lowercase
    return " ".join(hint)  # returns the hint list as a string with spaces between each character

def difficulty(level):
    if (level.lower() == "easy"):
        return "easy"

    if (level.lower() == "medium"):
        return "medium"

    if (level.lower() == "hard"):
        return "hard"

words = ["joseph", "moroni", "helaman", "luke", "mark", "john", "mathew", "alma", "amuleke"]  # a list of possible words for the game

level = input("Please select your difficulty (easy, medium or hard: )")

difficulty_level = difficulty(level.lower())

if (difficulty_level == "easy"):
    attempts = 0

    game = True  # flag to start the game loop

    while game:  # the main game loop, while the game flag is True
        secret_word = random.choice(words)  # selects a random word from the list

        print("Welcome to the word guessing game!\nYou have to try and find the secret word.\nRemember to count the number of letters from the hint!")  # prints the game instructions

        hint = "_" * len(secret_word)  # initializes the hint to underscores, using string multiplication to match the length of the secret word
        print(f"Your hint is: {hint}")  # prints the initial hint to the user

        count = 1  # counts the number of attempts, starting from 1

        while True:  # loop until the game is over
            guess = input("\nWhat is your guess? ").strip()  # gets user input and removes any leading/trailing whitespaces
            hint = get_hint(secret_word, guess)  # calls the get_hint() function to generate the new hint based on the guess
            print(f"Your hint is: {hint}")  # prints the new hint to the user

            if guess.lower() == secret_word.lower():  # checks if the user has guessed the correct word, regardless of case
                break
            
            count += 1  # increments the attempt count

            if len(guess) != len(secret_word):  # if the user's guess has a different length than the secret word, display an error message and the current hint
                print(f"Sorry, the guess must have the same number of letters as the secret word, which is {len(secret_word)}.\nYour hint is: {hint}")

        if (guess == secret_word):  # if the user has guessed the word 
            print("Congratulations! You guessed it!")
            print(f"It took you {count} guesses.")

        _continue = input("Would you like to play again? (YES or NO): ").strip().lower()  # asks if the user wants to play again
        if (_continue.lower() == "yes"):
            game = True
        elif (_continue.lower() == "no"):
            game = False
        else:
            _continue = input("Please type YES or NO: ")

elif (difficulty_level == "medium"):
    attempts = 7 # sets the allowed ammount of attempts for the user

    game = True  # flag to start the game loop

    while game:  # the main game loop, while the game flag is True
        secret_word = random.choice(words)  # selects a random word from the list

        print(f"Welcome to the word guessing game!\nYou have {attempts} attempts to try and find the secret word.\nRemember to count the number of letters from the hint!")  # prints the game instructions

        hint = "_" * len(secret_word)  # initializes the hint to underscores, using string multiplication to match the length of the secret word
        print(f"Your hint is: {hint}")  # prints the initial hint to the user

        count = 1  # counts the number of attempts, starting from 1

        while True:  # loop until the game is over
            guess = input("\nWhat is your guess? ").strip()  # gets user input and removes any leading/trailing whitespaces
            hint = get_hint(secret_word, guess)  # calls the get_hint() function to generate the new hint based on the guess
            print(f"Your hint is: {hint}")  # prints the new hint to the user

            if guess.lower() == secret_word.lower():  # checks if the user has guessed the correct word, regardless of case
                break
            
            count += 1  # increments the attempt count

            if count > attempts:  # if the user has exceeded the number of attempts, end the game
                print(f"Sorry you didn't find the word in time. The word was {secret_word}.")
                break

            if len(guess) != len(secret_word):  # if the user's guess has a different length than the secret word, display an error message and the current hint
                print(f"Sorry, the guess must have the same number of letters as the secret word, which is {len(secret_word)}.\nYour hint is: {hint}")

        if (count <= attempts):  # if the user has guessed the word 
            print("Congratulations! You guessed it!")
            print(f"It took you {count} guesses.")

        _continue = input("Would you like to play again? (YES or NO): ").strip().lower()  # asks if the user wants to play again
        if (_continue.lower() == "yes"):
            game = True
        elif (_continue.lower() == "no"):
            game = False
        else:
            _continue = input("Please type YES or NO: ")


elif (difficulty_level == "hard"):
    attempts = 4 # sets the allowed ammount of attempts for the user

    game = True  # flag to start the game loop

    while game:  # the main game loop, while the game flag is True
        secret_word = random.choice(words)  # selects a random word from the list

        print(f"Welcome to the word guessing game!\nYou have {attempts} attempts to try and find the secret word.\nRemember to count the number of letters from the hint!")  # prints the game instructions

        hint = "_" * len(secret_word)  # initializes the hint to underscores, using string multiplication to match the length of the secret word
        print(f"Your hint is: {hint}")  # prints the initial hint to the user

        count = 1  # counts the number of attempts, starting from 1

        while True:  # loop until the game is over
            guess = input("\nWhat is your guess? ").strip()  # gets user input and removes any leading/trailing whitespaces
            hint = get_hint(secret_word, guess)  # calls the get_hint() function to generate the new hint based on the guess
            print(f"Your hint is: {hint}")  # prints the new hint to the user

            if guess.lower() == secret_word.lower():  # checks if the user has guessed the correct word, regardless of case
                break
            
            count += 1  # increments the attempt count

            if count > attempts:  # if the user has exceeded the number of attempts, end the game
                print(f"Sorry you didn't find the word in time. The word was {secret_word}.")
                break

            if len(guess) != len(secret_word):  # if the user's guess has a different length than the secret word, display an error message and the current hint
                print(f"Sorry, the guess must have the same number of letters as the secret word, which is {len(secret_word)}.\nYour hint is: {hint}")

        if (count <= attempts):  # if the user has guessed the word 
            print("Congratulations! You guessed it!")
            print(f"It took you {count} guesses.")

        _continue = input("Would you like to play again? (YES or NO): ").strip().lower()  # asks if the user wants to play again
        if (_continue.lower() == "yes"):
            game = True
        elif (_continue.lower() == "no"):
            game = False
        else:
            _continue = input("Please type YES or NO: ")




print("Thanks for playing! Goodbye.") # the game is over, prints a goodbye message
