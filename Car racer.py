import random
import os


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


def roll_dice():
    return random.randint(1, 6)


car_choice = get_integer_input('Choose a car from 1 to 6 \n', 'Please choose a car from 1 to 6', 0, 7)


race_distance = get_integer_input('pick a race distance between 5 and 15 \n', 'Please enter an amount between 5 and 15', 4, 16)


cars = [0, 0, 0, 0, 0, 0]


while max(cars) < race_distance:
    for i, car in enumerate(cars):
        print ('-'*car + 'o-o')
    input('push enter to continue')
    os.system('cls')
    cars[roll_dice()-1] += 1