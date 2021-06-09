#BROKE
from random import choice
winnings = 0
token = ['unicorn', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse','zebra', 'zebra', 'horse', 'horse', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey', 'donkey']
for i in range(750):
    token.append('donkey')
rewards = {'donkey': 0, 'horse': 0.5, 'zebra': 0.5, 'unicorn': 5}

while True:
    print ('''
    ********************WELCOME TO THE LUCKY UNICORN GAME********************

    This is a chance game where you pay a dollar and you have the chance to win up to 5 dollars!

    *************************************************************************
    ''')

    valid = False
    while not valid:
        try:
            dollars = int(input('how much money would you like to gamble? \n'))
            if 0 < dollars <= 10:
                valid = True
            else:
                print ('please enter a whole amount between one and ten dollars')
        except ValueError:
            print('please enter a whole amount between one and ten dollars')
    while dollars > 0:
        dollars -= 1
        tokens = choice(token)
        reward = rewards[tokens]
        if tokens == 'horse' or tokens == 'zebra':
            print (f'Congratulations you got a {tokens} \nYou win ${reward} as a prize')
        elif token == 'donkey':
            print(f'unlucky you got a {tokens} \nYou dont win anything')
        elif tokens == 'unicorn':
            print(f'Congratulations you won a {tokens} \nThats worth {reward}')
        winnings += reward
        print(f'Your current winnings: ${winnings}. Money left: ${dollars}')
        replay = input('Press enter to play again. \nType exit to cash out. \n')
        if replay == 'exit' or dollars < 0:
            print('Thanks for playing. Come back later.')
            print (f'Here are your winnings of ${winnings + dollars}. \nSee you next time.')
            break