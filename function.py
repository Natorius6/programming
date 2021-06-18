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

coffees = get_integer_input("Please enter how many coffes you've had", "Please enter a whole number above 0", 0, 100)
print (f"you've had {coffees}")