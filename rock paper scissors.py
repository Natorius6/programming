from random import choice

def get_integer_input(message, error, low, high):
    while True:
        try:
            inpt = int(input(message))
            if low < inpt < high:
                return inpt
            else:
                print(error)
        except ValueError:
            print(error)


while True:
    options = ['Rock', 'Paper', 'Scissors']
    print('''
    ********************************************************************************
                            WELCOME TO THE ROCK PAPER SCISSORS GAME

                                    TRY TO BEAT THE AI
    ******************************************************************************** ''')
    Ai_won = 0
    Human_won = 0

    num_games = get_integer_input('how many games would you like to play? \n', 'Please input a number between 1 and 10000.', 0, 10001)
    while num_games != 0:
        human_choice = input("Rock, Paper or Scissors? \n")
        Ai_choice = choice(options)
        if human_choice == 'Rock':
            if Ai_choice == 'Rock':
                print ('you chose Rock, AI chose Rock. \nITS A TIE!')
                num_games -= 1
            if Ai_choice == 'Paper':
                print ('you chose Rock, AI chose Paper. \nYOU LOSE!')
                num_games -= 1
            if Ai_choice == 'Scissors':
                print ('you chose Rock, AI chose Scissors. \nYOU WIN!')
                num_games -= 1
        if human_choice == 'Paper':
            if Ai_choice == 'Rock':
                print ('You chose Paper, AI chose Rock. \nYOU WIN!')
                num_games -= 1
            if Ai_choice == 'Paper':
                print ('You chose Paper, AI chose Paper. \n ITS A TIE!')
                num_games -= 1
            if Ai_choice == 'Scissors':
                print ('You chose Paper, AI chose Scissors. \nYOU LOSE!')
                num_games -= 1
        if human_choice == 'Scissors':
            if Ai_choice == 'Rock':
                print ('You chose Scissors, AI chose Rock. \nYOU LOSE!')
                num_games -= 1
            if Ai_choice == 'Paper':
                print ('You chose Scissors, AI chose Paper. \nYOU WIN!')
                num_games -= 1
            if Ai_choice == 'Scissors':
                print ('You chose Scissors, AI chose Scissors. \nITS A TIE!')
                num_games -= 1