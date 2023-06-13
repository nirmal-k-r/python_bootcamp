import random

class Game:
    def __init__(self):
        self.possible_choices=["rock", "paper", "scissors"]


    def get_user_item(self):
        choice=""
        while choice!="rock" or choice!="paper" or choice!="scissors":
            choice=input("Enter your choice (rock/paper/scissors): ")
            if choice=="rock" or choice=="paper" or choice=="scissors":
                return choice   
            else:
                print("Invalid choice. Please try again.")

    def get_computer_item(self):
        return random.choice(self.possible_choices)

    def get_game_result(self, user_item, computer_item):
        winning_patterns=[["rock","scissors"], ["paper", "rock"], ["scissors", "paper"]]
        if user_item==computer_item:
            return "draw"
        else:
            for pattern in winning_patterns:   
                if user_item in pattern and computer_item in pattern:
                    if user_item==pattern[0]:
                        return "win"
                    else:
                        return "loss"
            

    def play(self):
        user_item=self.get_user_item()
        computer_item=self.get_computer_item()
        print(f"You selected {user_item}. The computer selected {computer_item}.")
        result=self.get_game_result(user_item, computer_item)
        if result=="win":
            print("You won!")
        elif result=="loss":
            print("You lost!")
        else:
            print("You drew!")
        
        return result