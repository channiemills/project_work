import numpy as np

choices = ['rock', 'paper', 'scissors']


def get_user_input():
    your_choice = raw_input('Rock, paper, or scissors?').lower()
    if your_choice in choices:
        return your_choice
    else:
        print 'Invalid selection. Choose rock, paper, or scissors.'
        get_user_input()


def game():
    your_choice = get_user_input()
    comp_choice = np.random.choice(choices,1)[0]
    loss_text = 'You lost! You chose ' + your_choice + ' and the computer chose ' + comp_choice
    if comp_choice == your_choice:
        print 'Tie! You both chose ' + your_choice
    elif your_choice == 'rock' and comp_choice == 'paper':
        print loss_text
    elif your_choice == 'paper' and comp_choice == 'scissors':
        print loss_text
    elif your_choice == 'scissors' and comp_choice == 'rock':
        print loss_text
    else:
        print 'You won! You chose ' + your_choice + ' and the computer chose ' + comp_choice
    play_again()


def play_again():
    replay = raw_input('Do you want to play again, yes or no?').lower()
    if replay == 'yes':
        game()
    elif replay == 'no':
        exit
    else:
        print 'Invalid response. Please type yes or no'
        play_again()

game()
