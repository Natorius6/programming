import random

while True:
    print('''
    ********************************************************************************
                             WELCOME TO THE HIGHER LOWER GAME
    
                             GUESS THE CORRECT NUMBER TO WIN
    ******************************************************************************** ''')
    num_guess = 0
    guess = int(input('what do you want the max number of guesses to be? \n'))
    start_num = int(input("what do you want the lowest number to be? \n"))
    end_num = int(input('what do you want the highest number to be? \n'))
    num = random.randrange(start_num, end_num + 1)
    inp = int(input("guess the number \n"))
    while inp != num:
        if inp < num:
            num_guess += 1
            print ("too low!")
            inp = int(input("guess the number \n"))
        if inp > num:
            num_guess += 1
            print ("too high!")
            inp = int(input("guess the number \n"))
        if num_guess == guess:
            print(f'you ran out of guesses \nThe number was {num}')
            break
        if inp == num:
            print (f"well done you got it in {num_guess} guesses")
            break