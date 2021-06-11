from random import choice
options = ['Rock', 'Paper', 'Scissors']
while True:
    print('''
    ********************************************************************************
                            WELCOME TO THE ROCK PAPER SCISSORS GAME

                                    TRY TO BEAT THE AI
    ******************************************************************************** ''')
    Ai_won = 0
    Human_won = 0
    num_games = int(input('how many games would you like to play? \n'))
    while num_games > 0:
        Ai_Choice = choice(options)
        Label:
        Human_Choice = input('Rock, Paper or Scissors? \n')
        if Human_Choice != 'rock' or 'paper' or 'scissors':
            print('please enter Rock, Paper or Scissors')
            goto Label;
        if Human_Choice == 'rock' or 'paper' or 'scissors':
            print(f'{Ai_Choice}')