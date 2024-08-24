import random

def get_user_choice():
    choice=input(f"Enter your Choice[R,P,S]:").upper()
    while choice not in ["R","P","S"]:
        print("Please enter a valid input.")
        choice=input(f"Enter your Choice[R,P,S]:").upper()
    return choice

def get_computer_choice():
    computer=random.choice(["R","P","S"]).upper()
    return computer

def result(user_choice,computer_choice):
    '''
    user_choice=get_user_choice()
    computer_choice=get_computer_choice() '''
    
    #print(f"\nUser choose {Dict[user_choice]} and computer chose {Dict[computer_choice]}")
    if user_choice==computer_choice:
        print(f"Both have same choice, it's a tie!")
    elif (user_choice == "R" and computer_choice == "S") or \
         (user_choice == "P" and computer_choice == "R") or \
         (user_choice == "S" and computer_choice == "P"):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    Dict={"R":"Rock","P":"Paper","S":"Scissor"}
    print(f"You chose:{Dict[user_choice]}")
    print(f"Computer chose:{Dict[computer_choice]}")
    
    winner = result(user_choice, computer_choice)
    print(winner)

if __name__ == "__main__":
    play_game()