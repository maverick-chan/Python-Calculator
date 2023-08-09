#Number Mystery v1.0

import random
random_number = random.randint(1,10)
active = True
counter = 0
score = 1

print("Welcome to Number Mystery! Your job is to guess what number Python is thinking in the least number of guesses possible.")
name = input("Please enter your name to continue: ")

while active:
    insert_number = int(input("Please guess a number between 1 and 10: "))
    if insert_number == random_number:
        print("\nCongratulations! You have guessed the correct number!")
        print(f"Your high-score was {score} guesse(s).")
        repeat = input("\nWould you like to play again? (yes/no): ")
        if repeat == 'yes':
            score = 1
            counter = 0
            random_number = random.randint(1,10)
        elif repeat == 'no':
            break
    elif insert_number <= 0 or insert_number > 10:
        print("\tPlease enter a number from 1 to 10.")
    else:
        counter += 1
        score += 1
        remaining_lives = 3 - counter
        print(f"\tPlease try again. You have {remaining_lives} lives remaining") 

        if counter == 3:
            end = input("\nSorry, you have lost. Would you like to try again? (yes/no): ")
            if end == 'yes':
                counter = 0
            if end == 'no':
                break

leaderboard = {}
leaderboard[name.title()] = score
sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)[:3])
print("\nLeaderboard:")
print(sorted_leaderboard)