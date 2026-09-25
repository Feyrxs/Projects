import random

print("Lets play rock paper scissors!")

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

game_image = [rock, paper, scissors]

while True:
    try:
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").strip())

        print(game_image[user_choice])

        computer_choice = random.randint(0, 2)
        print(f"Computer chose: {game_image[computer_choice]}")

        if user_choice == computer_choice:
            print("Its a draw!")

        elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
            print ("You win!")

        else:
            print ("You lose!")

        go_again = input ("Would you like to go again? 'yes' or 'no'\n").strip().lower()
        if go_again == "yes":
            continue
        else:
            print("Goodbye, friend!")
            break

    except ValueError:
        print("That's not a number! Try again.")
    except IndexError:
        print("Invalid choice! Try again.")

