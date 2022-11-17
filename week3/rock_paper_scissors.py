import random
import numpy as np

user_vs_machine = 1
user_vs_user = 2


def random_option():
    a = random.choice(['R', 'P', 'S'])
    return a


def game_with_user():
    lis_score = [0, 0]
    while max(lis_score) < 3:
        user_1 = input('choose among for user1 R,P,S:')
        user_2 = input('choose among for user2 R,P,S:')
        if user_1 == 'R' and user_2 == 'S':
            lis_score[0] += 1
        elif user_1 == 'S' and user_2 == 'P':
            lis_score[0] += 1
        elif user_1 == 'P' and user_2 == 'R':
            lis_score[0] += 1
        elif user_2 == 'R' and user_1 == 'S':
            lis_score[1] += 1
        elif user_2 == 'S' and user_1 == 'P':
            lis_score[1] += 1
        elif user_2 == 'P' and user_1 == 'R':
            lis_score[1] += 1
        elif user_1 == user_2:
            print("Draw")
            continue
        else:
            print('invalid input  .')
        if lis_score[0] > lis_score[1]:
            print('winner is user1,', lis_score[0])
        else:
            print('winner is user2,', lis_score[1])


def game_with_machine():
    lis1_scores = [0, 0]
    while max(lis1_scores) < 3:
        user = input('choose among R,P,S:')
        machine = random_option()
        print('machine choice is:', machine)
        if user == 'R' and machine == 'S':
            lis1_scores[0] += 1
        elif user == 'S' and machine == 'P':
            lis1_scores[0] += 1
        elif user == 'P' and machine == 'R':
            lis1_scores[0] += 1
        elif machine == 'R' and user == 'S':
            lis1_scores[1] += 1
        elif machine == 'S' and user == 'P':
            lis1_scores[1] += 1
        elif machine == 'P' and user == 'R':
            lis1_scores[1] += 1
        elif machine == user:
            print("Draw")
            continue
        else:
            print('invalid input!')
        if lis1_scores[0] > lis1_scores[1]:
            print('winner is user,', lis1_scores[0])
        else:
            print('winner is machine,', lis1_scores[1])


def input_user():
    choice = input('enter 1 if you want to play with computer\nenter 2 if you want to play with other player: ')
    if choice == '1':
        game_with_machine()
    elif choice == '2':
        game_with_user()
    else:
        return 'invalid input'


input_user()
