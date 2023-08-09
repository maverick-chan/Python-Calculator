#Number Mystery v4.1

import random

print("Welcome to Number Mystery v4.1! \nGuess the number in the least number of guesses possible.")

leaderboard = {}
status = True

while status:
    name = input("\nPlease enter your name to continue (or 'q' to quit): ")
    if name.lower() == 'q':
        break

    min_num = 1
    max_num = 20
    random_number = random.randint(min_num, max_num)   

    scores = []
    score = 1
    counter = 0
    active = True

    while active:
        print("\n-----------------------------------------------------")
        guess = (input(f"Enter a number between {min_num} & {max_num}: "))
        if guess.lower() == 'q':
            status = False
            break
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        else:
            if guess < min_num or guess > max_num:
                print(f"Invalid input. Please enter a number from {min_num} to {max_num}.")

            elif guess == random_number:
                print("\n-----------------------------------------------------")
                print("Congratulations! You have guessed the correct number!")
                print(f"Your high-score was {score} guess(es).")
                scores.append(score)

                if name.title() not in leaderboard:
                    leaderboard[name.title()] = []
                leaderboard[name.title()].extend(scores)
                
                sorted_leaderboard = {name: min(scores) for name, scores in leaderboard.items()}
                top_leaderboard = dict(sorted(sorted_leaderboard.items(), key=lambda item: item[1], reverse=False)[:3])
                print("\nTop 3 Leaderboard:")
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

    while True:
        repeat = input("\nWould you like to play again? (yes/no): ")
        if repeat.lower() == 'no':
            status = False
            break
        elif repeat.lower() == 'yes':
            score = 1
            counter = 0
            scores = []
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")