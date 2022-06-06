import random


user_action = input ("Enter a choice (R, P, S): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
    #print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
while True:
    if user_action == "R":
        user_action = "rock"
    elif user_action == "P":
        user_action = "paper"
    elif user_action == "S":
        user_action = "scissors"
    elif user_action not in possible_actions:
        print("invalid option")
        user_action = input("enter a choice(R, P or S): ")

    
        
    elif user_action == computer_action:
        print(f"player({user_action}): computer({computer_action})")
        print(f"both players selected {user_action}, therefore it is a tie")
        print("play again")
        user_action = input("enter a choice(R, P or S): ")
        computer_action = random.choice(possible_actions)
        continue
    else:
        print(f"player({user_action}): computer({computer_action})")
        if user_action == "rock":
            if computer_action == "scissors":
                print("you win")
            else:
                print("you lose")
        elif user_action == "paper":
            if computer_action == "rock":
                print("you win")
            else:
                print("you lose")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("you win")
            else:
                print("you lose")
        print("Game over")
        break