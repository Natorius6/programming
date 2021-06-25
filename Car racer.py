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

def roll_two_dice():
    return roll_dice() + roll_dice()

def roll_dice():
    return random.randint(1, 6)

cars = []
for i in range (12):
    cars.append(0)

car_choice = get_integer_input(f'Choose a car from 1 to {len(cars)} \n', f'Please choose a car from 1 to {len(cars)}', 0, len(cars) + 1)


race_distance = get_integer_input('pick a race distance between 5 and 15 \n', 'Please enter an amount between 5 and 15', 4, 16)




while len([i for i in cars if i >= 15]) < 3:
    for i, car in enumerate(cars):
        if i == car_choice - 1 and car < 15:
            print('\033[1;32;40m' + '-' * car + 'o=o')
        else:
            print('\033[1;31;40m' + '-' * car + 'o=o')
    input('push enter to continue')
    os.system('cls')
    cars[roll_two_dice()-1] += 1

sorted_cars = sorted(cars)
winning_car = cars.index(max(cars)) + 1
print(f"Car {winning_car} won!")


if winning_car == car_choice:
    print("well done your car won")
else:
    print("oh no your car didn't win, better luck next time.")