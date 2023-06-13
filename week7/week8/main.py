import os
from game import Game

game=Game()
results={
    "win": 0,
    "loss": 0,
    "draw": 0
}


def get_user_menu_choice():
    # os.system("clear")
    print("\n\nChoose an option:")
    print("1 - Play a new game")
    print("2- Show scores")
    print("3- Quit")
    choice=input("Enter your choice: ")
    return choice

def print_results(results):
    print("Wins: ", results["win"])
    print("Losses: ", results["loss"])
    print("Draws: ", results["draw"])


def main():
    choice=""
    while choice!="1" or choice!="2" or choice!="3":
        choice=get_user_menu_choice()
        if choice=="1":
            result=game.play()
            if result=="win":
                results["win"]+=1
            elif result=="loss":
                results["loss"]+=1
            else:
                results["draw"]+=1
        elif choice=="2" or choice=="q":
            print_results(results)
        elif choice=="3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

main()