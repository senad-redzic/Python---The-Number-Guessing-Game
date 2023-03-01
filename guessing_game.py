"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random
highest_scores = []

def start_game():
    print("""
    Your goal is to guess the random number between 1 and 10.
    Good luck! 
    """)
    # Generating rundom number
    random_number = random.randrange(1, 11)
    number_of_attempts = 0
    # Starting while loop that contains all steps of the game
    while True: 
        try:
            new_guess = input("Guess the number:  ")
            new_guess = int(new_guess)
            number_of_attempts += 1
            
            # If user gets the number
            if new_guess == random_number:
                # Saving the number of attempts to the list
                highest_scores.append(number_of_attempts)
                
                print("You got it!")
                print("It took you a {} attempts to guess the number".format(number_of_attempts))
                print("Thanks for playing!")
                # Asking user if he/she wants to play again
                play_again = input("Do you want to play again? Y/N   ")
                if play_again.lower() == "y": 
                    # Saving the number of attempts to the list
                    highest_scores.append(number_of_attempts)
                    #Getting the highest score/the lowest number from the list
                    highest_score = min(highest_scores)
                    print("The current best score is {} attempts. ".format(highest_score))
                    if highest_score == 1:
                        print("Great job! You achieved the best possible result")
                    start_game()
                else:
                    print("OK. Have a nice day!")
                    break
            # If user enters bigger number but not bigger than 10
            elif new_guess > random_number and new_guess <= 10:
                print("It's lower")
            # If user enters lower number but not lower than 1    
            elif new_guess < random_number and new_guess >= 1:
                print("It's higher")
            # If user enters a number bigger than 10
            elif new_guess > 10:
                print("{} is out of range. The number is in a range between 1 and 10!".format(new_guess))
            # If user enters a number lower than 1    
            elif new_guess < 1:
                print("{} is out of range. The number is in a range between 1 and 10!".format(new_guess))
        except ValueError:
            print("You can only insert number between 1 and 10!")

# Calling the function
start_game()
