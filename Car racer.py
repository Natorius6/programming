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


winning_car = cars.index(max(cars)) + 1
print(f"Car {winning_car} won!")


if winning_car == car_choice:
    print("well done your car won")
else:
    print("oh no your car didn't win, better luck next time.")