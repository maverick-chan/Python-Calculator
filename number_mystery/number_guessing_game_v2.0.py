#Number Mystery v2.0

import random

leaderboard = {}

print("Welcome to Number Mystery! Your job is to guess what number Python is thinking in the least number of guesses possible.")

while True:
    name = input("Please enter your name to continue (or 'q' to quit): ")
    if name.lower() == 'q':
        break

    random_number = random.randint(1, 10)
    active = True
    counter = 0
    score = 1

    while active:
        insert_number = int(input("Please guess a number between 1 and 10: "))

        if insert_number == random_number:
            print("\nCongratulations! You have guessed the correct number!")
            print(f"Your high-score was {score} guess(es).")

            leaderboard[name.title()] = score

            repeat = input("\nWould you like to play again? (yes/no): ")
            if repeat.lower() == 'yes':
                score = 1
                counter = 0
                random_number = random.randint(1, 10)
            elif repeat.lower() == 'no':
                active = False

        elif insert_number <= 0 or insert_number > 10:
            print("\tPlease enter a number from 1 to 10.")

        else:
            counter += 1
            score += 1
            remaining_lives = 3 - counter
            print(f"\tPlease try again. You have {remaining_lives} lives remaining")

            if counter == 3:
                print("\nSorry, you have lost.")
                active = False

sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)[:3])
print("\nLeaderboard:")
print(sorted_leaderboard)
