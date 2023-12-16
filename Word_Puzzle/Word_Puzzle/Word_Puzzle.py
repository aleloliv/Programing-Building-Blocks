#implemented a list of words that the games randomly picks from, added a while loop to continue the game if the player desires to, added a limit on the number of attempts only if the player doesn't choose easy mode, in easy mode the game continues indefinitely. Defined a function to return the hint following the rules. Also defined functions to pick difficulty, and to play the game itself.

# Import the random module for word selection
import random

# Function to generate the hint based on the secret word and the guess
def get_hint(word, guess):
    hint = ["_" for _ in word]
    for i, letter_g in enumerate(guess):
        if letter_g.lower() in word.lower():
            if letter_g.lower() == word[i].lower():
                hint[i] = letter_g.upper()
            else:
                hint[i] = letter_g.lower()
    return " ".join(hint)

# Function to get the desired difficulty level from the user
def get_difficulty():
    while True:
        level = input("Please select your difficulty (easy, medium, or hard): ").lower()
        if level in ["easy", "medium", "hard"]:
            return level
        else:
            print("Invalid difficulty level. Please try again.")

# Function to play the game
def play_game(words):
    game = True

    while game:
        # Get the desired difficulty level
        difficulty = get_difficulty()
        attempts = 0
        
        # Set the number of attempts based on the selected difficulty
        if difficulty == "easy":
            attempts = float('inf')  # Infinite attempts for easy level
        elif difficulty == "medium":
            attempts = 7  # 7 attempts for medium level
        elif difficulty == "hard":
            attempts = 4  # 4 attempts for hard level
        
        # Select a random secret word from the list
        secret_word = random.choice(words)
        hint = "_" * len(secret_word)
        print(f"Welcome to the word guessing game!\nYou have {attempts} attempts to try and find the secret word.")
        print(f"Your hint is: {hint}")
        
        count = 0
        guessed = False
        
        # Loop to get guesses until the word is guessed or attempts run out
        while count < attempts and not guessed:
            count += 1
            guess = input("\nWhat is your guess? ").strip().lower()
            
            # Check if the guess is correct
            if guess == secret_word:
                guessed = True
            # Check if the guess has the same length as the secret word
            elif len(guess) != len(secret_word):
                print(f"Sorry, the guess must have the same number of letters as the secret word, which is {len(secret_word)}.\nYour hint is: {hint}")
            else:
                # Update the hint based on the guess
                hint = get_hint(secret_word, guess)
                print(f"Your hint is: {hint}")
        
        # Display the result of the game
        if guessed:
            print("Congratulations! You guessed it!")
        else:
            print(f"Sorry, you didn't find the word in time. The word was {secret_word}.")
        
        # Display the number of attempts made
        print(f"It took you {count} attempts.")
        
        # Ask the player if they want to play again
        play_again = input("Would you like to play again? (YES or NO): ").strip().lower()
        while play_again not in ["yes", "no"]:
            play_again = input("Please type YES or NO: ").strip().lower()
        
        # Check if the player wants to continue playing
        if play_again == "no":
            game = False

    print("Thanks for playing! Goodbye.")

# List of words for the game
words = ["joseph", "moroni", "helaman", "luke", "mark", "john", "matthew", "alma", "amulek",
         "genesis", "exodus", "leviticus", "numbers", "deuteronomy", "joshua", "judges", "ruth", "1 samuel", "2 samuel",
         "1 kings", "2 kings", "1 chronicles", "2 chronicles", "ezra", "nehemiah", "esther", "job", "psalms", "proverbs",
         "ecclesiastes", "song of solomon", "isaiah", "jeremiah", "lamentations","ezekiel", "daniel", "hosea", "joel", "amos", "obadiah", "jonah", "micah", "nahum", "habakkuk", "zephaniah", "haggai",
         "zechariah", "malachi", "1 nephi", "2 nephi", "jacob", "enos", "jarom", "omni", "words of mormon", "mosiah", "alma",
         "helaman", "3 nephi", "4 nephi", "mormon", "ether", "moroni", "matthew", "mark", "luke", "john", "acts", "romans",
         "1 corinthians", "2 corinthians", "galatians", "ephesians", "philippians", "colossians", "1 thessalonians",
         "2 thessalonians", "1 timothy", "2 timothy", "titus", "philemon", "hebrews", "james", "1 peter", "2 peter",
         "1 john", "2 john", "3 john", "jude", "revelation", "moses", "abraham", "joseph smith matthew", "joseph smith history",
         "articles of faith"]

# Start the game
play_game(words)
