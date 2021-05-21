from replit import clear
import random
import art
from game_data import data


def print_account(account):
    """Converts account data to be printed."""
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description}, from {country}."


def check_guess(a_followers, b_followers, guess):
    """Gets the highest follower count and compares it with player Guess. If equal return True. If not return False."""
    if a_followers > b_followers and guess == "A":
        return True
    elif a_followers < b_followers and guess == "B":
        return True


def play(account_a, account_b, player_score):
    """Show options and ask for player guess. If player guess is right continue. If not ends."""
    clear()

    print(art.logo)

    if player_score != 0:
        print(f"You're right! Current score: {player_score}.")
    # Showing participants
    print(f"Compare A: {print_account(account_a)}.")

    print(art.vs)

    print(f"Against B: {print_account(account_b)}.")

    # Ask to the player for its guess
    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    is_correct = check_guess(account_a["follower_count"], account_b["follower_count"], guess)

    if is_correct:
        player_score += 1

        account_a = account_b
        account_b = random.choice(data)

        play(account_a, account_b, player_score)
    else:
        print(f"Sorry, that's wrong. Final score: {player_score}")


def init():
    # Initial data
    options = random.sample(data, 2)
    option_a = options[0]
    option_b = options[1]
    score = 0
    # Start game
    play(option_a, option_b, score)

init()