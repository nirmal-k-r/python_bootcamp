#melanie
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Scissors

from random import choice


def game(command, score_value):
    game_list = ['rock', 'paper', 'scissors']
    if command not in game_list:
        print('Invalid input!')
        return int(score_value)
    game_dict = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
    ai_command = game_dict[choice(game_list)]
    if command == ai_command:
        print(f'There is a draw ({ai_command})')
        return int(int(score_value) + 50)
    elif command == game_dict[ai_command]:
        print(f"Well done. The computer chose {ai_command} and failed")
        return int(int(score_value) + 100)
    elif ai_command == game_dict[command]:
        print(f"Sorry, but the computer chose {ai_command}")
        return int(score_value)


def advanced_game(raw_list, user_choice, score):
    game_list = raw_list.replace(" ", "").split(',')
    draw_element = ''
    win_list = []
    lose_list = game_list.copy()
    command = user_choice
    if command not in game_list:
        print('Invalid input!')
        return int(score)
    elif command in game_list:
        element_index = lose_list.index(command)
        draw_element = lose_list.pop(element_index)
        half_length = int(len(lose_list) / 2)
        for i in range(half_length):
            coord = element_index - i
            if coord <= 0:
                win_list.append(lose_list.pop())
            else:
                win_list.append(lose_list.pop(coord - 1))
    ai_choice = choice(game_list)
    if ai_choice == draw_element:
        print(f'There is a draw ({ai_choice})')
        return int(int(score) + 50)
    elif ai_choice in win_list:
        print(f"Well done. The computer chose {ai_choice} and failed")
        return int(int(score) + 100)
    elif ai_choice in lose_list:
        print(f"Sorry, but the computer chose {ai_choice}")
        return int(score)


"""def get_rating(name):
    with open('rating.txt', 'r') as rate:
        for line in rate:
            if line.startswith(name):
                temp = line.split()
                return temp[1]
    return 0"""


def main():
    user_name = input("Enter your name: ")
    print(f'Hello, {user_name}.')
    print('Print "Enter" to play regular rules, or input your own elements comma separated.')
    game_variant = input()
    print("Okay, let's start")
    score = 0
    user_choice = input()
    while user_choice != '!exit':
        if user_choice != '!rating':
            if game_variant == '':
                score = game(user_choice, score)
            else:
                score = advanced_game(game_variant, user_choice, score)
        else:
            print(score)
        user_choice = input()
    else:
        print('Bye!')


main()