import random

import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# putting the variables in a list called choices
choices = [rock, paper, scissors]

while True:
    # initializing scores
    user_score = 0
    computer_score = 0

    while True:
        try:
            # getting the user input
            user_choice = input('\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ')

            # validate if input is an integer
            if not user_choice.isdigit():
                raise ValueError("Invalid input. Please enter a valid integer.")

            # convert user input to integer
            user_choice = int(user_choice)

            # validate if input is within the range of 0 to 2
            if user_choice < 0 or user_choice > 2:
                raise ValueError("Invalid input. Please choose a number between 0 and 2.")

            print(choices[user_choice])

            # generating a new random choice for the computer
            computer_choice = random.randint(0, 2)

            # adding a delay of 1 second before displaying the computer's choice
            time.sleep(1)

            # printing the computer choice based on the generated random number.
            print('Computer chose:')
            print(choices[computer_choice])

            if user_choice == 0 and computer_choice == 2:
                print('You win!')
                user_score += 1
            elif computer_choice == 0 and user_choice == 2:
                print('You lose!')
                computer_score += 1
            elif user_choice > computer_choice:
                print('You win!')
                user_score += 1
            elif computer_choice > user_choice:
                print('You lose!')
                computer_score += 1
            else:
                print("It's a draw!")

            # display scores
            print(f"\nYour score: {user_score}")
            print(f"Computer score: {computer_score}")

        except ValueError as e:
            print(str(e))

        # ask the user if they want to play again
        play_again = input("\nDo you want to play again? Enter 'no' to exit or any other key to play again : ")
        if play_again.lower() == "no":
            break

