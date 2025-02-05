#ROCK PAPER SCISSORS

#random.choice()

import random
inputs =['rock','paper','scissors']
user_choice=input('your choice:').lower()
if user_choice not in inputs:
    print('invalid input. Try  again')
else:
    comp_choice=random.choice(inputs)
    print(comp_choice)
    if comp_choice==user_choice:
        print('its a draw')
    elif comp_choice=='rock' and user_choice=='scissors':
        print('you lose:P')
    elif comp_choice=='paper' and user_choice=='rock':
        print('you lose:P')
    elif comp_choice=='scissors' and user_choice=='paper':
        print('you lose:P')
    else:
        print('you have won!')