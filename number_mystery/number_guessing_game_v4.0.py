#Number Mystery v4.0

import random

print("Welcome to Number Mystery! \nGuess the number in the least number of guesses possible.")

leaderboard = {}

while True:
    name = input("\nPlease enter your name to continue (or 'q' to quit): ")
    if name.lower() == 'q':
        break

    min_num = 1
    max_num = 20
    counter = 0
    score = 1
    active = True
    random_number = random.randint(min_num, max_num)   
    print(random_number)

    scores = []

    while active:
        print("\n-----------------------------------------------------")
        guess = (input(f"Enter a number between {min_num} & {max_num}: "))
        
        if guess.lower() == 'q':
            break

        elif int(guess) < min_num or int(guess) > max_num:
            print(f"Please enter a number from {min_num} to {max_num}.")

        elif int(guess) == random_number:
            print("\n-----------------------------------------------------")
            print("Congratulations! You have guessed the correct number!")
            print(f"Your high-score was {score} guess(es).")
            scores.append(score)

            if name.title() not in leaderboard:
                leaderboard[name.title()] = []
            leaderboard[name.title()].extend(scores)
            
            sorted_leaderboard = {name: min(scores) for name, scores in leaderboard.items()}
            top_leaderboard = dict(sorted(sorted_leaderboard.items(), key=lambda item: item[1], reverse=False)[:3])
            print("\nLeaderboard:")
            for key, value in top_leaderboard.items():
                print(f"{key}: {value}")

            active = False

        else:
            counter += 1
            score += 1
            remaining_lives = 5 - counter
            delta = random_number - int(guess)

            if counter == 5:
                print("\n-----------------------------------------------------")
                print("Sorry, you have lost.")
                active = False
            
            elif abs(delta) <= 4:
                print("\nClose! Try again.")
                print(f"Please try again. You have {remaining_lives} lives remaining")
            elif 4 < abs(delta) <= 8:
                print("\nGetting warmer!. Try again.")
                print(f"Please try again. You have {remaining_lives} lives remaining")
            elif 8 < abs(delta) <= 12:
                print("\nNote quite. Try again.")
                print(f"Please try again. You have {remaining_lives} lives remaining")
            elif 12 < abs(delta) <= 16:
                print("\nGetting colder! Try again.")
                print(f"Please try again. You have {remaining_lives} lives remaining")
            elif abs(delta) > 16:
                print("\nAre you even trying?. Try again.")
                print(f"Please try again. You have {remaining_lives} lives remaining")


    repeat = input("\nWould you like to play again? (yes/no): ")
    if repeat.lower() == 'no':
        break
    elif repeat.lower() == 'yes':
        score = 1
        counter = 0
        scores = []


