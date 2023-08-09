#Number Mystery v3.0

import random

print("Welcome to Number Mystery! \nGuess the number in the least number of guesses possible.")

leaderboard = {}

while True:
    name = input("\nPlease enter your name to continue (or 'q' to quit): ")
    if name.lower() == 'q':
        break

    min_num = 1
    max_num = 25
    counter = 0
    score = 1
    active = True

    random_number = random.randint(min_num, max_num)   
    print(random_number)

    while active:
        print("\n-----------------------------------------------------")
        guess = int(input(f"Enter a number between {min_num} & {max_num}: "))

        if guess < min_num or guess > max_num:
            print(f"\tPlease enter a number from {min_num} to {max_num}.")

        elif guess == random_number:
            print("\n-----------------------------------------------------")
            print("Congratulations! You have guessed the correct number!")
            print(f"Your high-score was {score} guess(es).")

            active = False
            leaderboard[name.title()] = score
            sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=False)[:3])
            print("\nLeaderboard:")
            print(sorted_leaderboard)

        else:
            counter += 1
            score += 1
            remaining_lives = 5 - counter
            delta = random_number - guess

            if counter == 5:
                print("\n-----------------------------------------------------")
                print("Sorry, you have lost.")
                active = False
            elif delta < 0:
                print("\nToo high. Try again.")
                print(f"Please try again. You have {remaining_lives} lives remaining")
            elif delta > 0:
                print("\nToo low. Try again.")
                print(f"Please try again. You have {remaining_lives} lives remaining")


    repeat = input("\nWould you like to play again? (yes/no): ")
    if repeat.lower() == 'no':
        break
    elif repeat.lower() == 'yes':
        score = 1
        counter = 0



