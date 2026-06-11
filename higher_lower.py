# Import data and logo
from higher_lower_art import logo, vs
from higher_lower_data import data
import random
### Making functions ###
def clear():
    """ Clears the previous values from the screen by printing 50 empty lines"""
    print("\n" * 50)

def random_extract(selection):
    """Extract the individual values from the random choices and return an f string"""
    name = selection['name']
    description = selection['description']
    country = selection['country']
    return f"{name}, a {description}, from {country}."

def get_answer(followers_a, followers_b):
    """Compares if A >= B and returns the resulting winning string"""
    if followers_a >= followers_b:
        return 'a'
    else:
        return 'b'

def higher_lower():
    #This is the main game, True by default.
    keep_playing = True
    score = 0

    # Get the first random value: b.
    compare_b = random.choice(data)

    while keep_playing:
        ### Get the values from the lists ###
        # As b is defined before, a becomes b and b is selected again.
        compare_a = compare_b
        compare_b = random.choice(data)
        # While loop to avoid duplicate results to compare
        while compare_a == compare_b:
            compare_b = random.choice(data)
        # Assign the number of followers to separate variables to compare later.
        followers_a = compare_a['follower_count']
        followers_b = compare_b['follower_count']
        print(logo)
        print(f"Compare A: {random_extract(compare_a)}")
        print(vs)
        print(f"Against B: {random_extract(compare_b)}")

        # Get the user input A or B
        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        while user_input != 'a' and user_input != 'b':
            user_input = input("Please select a valid option. Type 'A' or 'B': ").lower()
        # Compare the sum of followers and return the winning string value 'a' or 'b'
        is_correct = get_answer(followers_a, followers_b)
        # If a is correct it takes the value of b so it later (once the game starts again) becomes a.
        if user_input == is_correct:
            score += 1
            keep_playing = True
            clear()
            print(f"You're right! Your current score is: {score}")
            if is_correct == 'a':
                compare_b = compare_a
        else:
            keep_playing = False
            print(f"You're wrong! Final score: {score}")
    # if the game is lost, ask the user if they want to play again or end the game.
    if not keep_playing:
        play_again = input("Would you like to play again? ('y' or 'n'): ").lower()
        while play_again != 'y' and play_again != 'n':
            play_again = input("Invalid option. Please select 'y' or 'n': ").lower()
        if play_again == 'y':
            higher_lower()
        else:
            print("Goodbye!")

higher_lower()