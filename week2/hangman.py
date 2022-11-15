"""
first part:
"""
from helper_hangman import *
import random


def update_word_pattern(word, pattern, letter):
    empty = ''
    lis1 = []
    for i in range(len(word)):
        if word.startswith(letter, i):
            lis1.append(i)
    lis = list(pattern)
    for i in lis1:
        lis[i] = letter
    str1 = empty.join(lis)

    return str1


def run_single_game(list_words, score):
    guessed_letters = []
    wrong_guess_lst = []
    word = get_random_word(list_words)
    pattern = '_' * len(word)
    letter_count = 1
    msg = 'enter your letter'

    while score > 0 and '_' in pattern:
        display_state(pattern, wrong_guess_lst, score, msg)
        user_input = get_input()

        if user_input[0]==1 and len(str(user_input[1])) > 1:
            msg = 'incorrect input! but,no points deducted'
            guessed_letters.append(user_input[1])
            continue
        if user_input[0]==1 and not user_input[1].islower():
            msg = 'incorrect input! but,no points deducted'
            guessed_letters.append(user_input[1])
            continue
        if user_input[0]==1 and not user_input[1].isalpha():
            msg = 'incorrect input! but,no points deducted'
            guessed_letters.append(user_input[1])
            continue
        if user_input[1] in guessed_letters:
            msg = 'already guessed! but,no points deducted'
            guessed_letters.append(user_input[1])
            continue
        if user_input[0]==1 and str(user_input[1]) in word:
            score=score-1
            pattern = update_word_pattern(word, pattern, user_input[1])
            n=word.count(user_input[1])
            score = score + (n * (n + 1)) / 2
            guessed_letters.append(user_input[1])
            msg="Guess next letter"
            continue
        if user_input[0]==1 and str(user_input[1]) not in word:
            wrong_guess_lst.append(user_input[1])
            score = score - 1
            guessed_letters.append(user_input[1])
            msg="Wrong Guess! Try Again"
            continue
        if user_input[0] == 2:
            score = score - 1
            if word == user_input[1]:
                m = pattern.count('_')
                score = score + (m * (m + 1)) / 2
                print("Before:"+pattern)
                pattern=word
                print("After:"+pattern)
                continue
        if user_input[0] == 3:
            msg = 'one of the letter is: ' + word[random.randrange(0, len(word))]
            continue
    if score <= 0:
        msg = 'Lost the game!', word
    else:
        msg= "Won the Game"
    display_state(pattern, wrong_guess_lst, score, msg)
    return score


def main():
    words_list=load_words(file='words_list.txt')
    score=POINTS_INITIAL
    total_games =1
    while True:
        new_score = run_single_game(words_list, score)
        print("You finished the game, after " +str(total_games)+ " game your total score is "+ str(new_score))
        if new_score>0:
            checker=play_again("Do you want to play again?")
            score=new_score
            if checker:
                continue
            else:
                break
        if new_score == 0:
            checker = play_again("Do you want to play a new game with scores reset?")
            score = POINTS_INITIAL
            total_games = 0
            if checker:
                continue
            else:
                break



if __name__ == "__main__":
    main()


