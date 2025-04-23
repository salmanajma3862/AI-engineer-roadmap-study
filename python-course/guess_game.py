secret_word = "python"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
# The code above defines a function that takes three numbers as input and returns the maximum of the three. It then calls the function with three numbers and prints the result.

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        print("You have " + str(guess_limit - guess_count) + " tries left.")
        guess = input("Guess the secret word:")
        guess_count += 1
    else:
        out_of_guesses = True
    # The code above defines a function that takes three numbers as input and returns the maximum of the three. It then calls the function with three numbers and prints the result.
    if out_of_guesses:  # The code above defines a function that takes three numbers as input and returns the maximum of the three. It then calls the function with three numbers and prints the result.
        print("You have exceeded the number of tries!")
    if guess == secret_word:
        print("Congratulations! You guessed the word.")
    else:
        print("Try again!")
# The code above is a simple word guessing game. The user is prompted to guess the secret word, which is "python". If the guess is correct, a congratulatory message is displayed. If the guess is incorrect, the user is prompted to try again.