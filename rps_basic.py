#ROCK PAPER SCISSORS

import tkinter as tk
import random
from tkhtmlview import HTMLLabel

def gaming():
    user = user_choice.get()
    print('user:',user)

    choice = ['rock','paper','scissors']
    comp_choice = random.choices(choice)[0]
    print('comp:',comp_choice)
    
    if user.lower() in choice:
        if comp_choice == user.lower():
            l=tk.Label(text='draw')
            print('draw')

        elif (comp_choice == 'rock' and user.lower() == 'paper') or (comp_choice == 'paper' and user.lower() == 'scissors'):
            l=tk.Label(text='user wins')
            print('user wins')

        else:
            l=tk.Label(text='comp wins')
            print('comp wins')
    else:
        l=tk.Label(text='wrong input. Change the input!')
        print('wrong input!')
    
    l.pack()    
    
        

window = tk.Tk()
window.title('rock paper scissors')
window.geometry('1270x680')

line = HTMLLabel(window, html = "\
                 <h1 style='color:red;'><b>hi! ITs the rock paper scissors game!</b></h1>\
                 <img src='https://i.ytimg.com/vi/Z13kiomZvak/maxresdefault.jpg'>\
                 <h2>Give your input</h2><h6>rock/paper/scissors</h6>\
                 ")


line.pack(fill='both',expand='true')

l1 = tk.Label(text='user-choice: ')
l1.pack()
user_choice = tk.StringVar()
e1 = tk.Entry(textvariable = user_choice)
e1.pack()



b1 = tk.Button(text = 'result', command = gaming)
b2 = tk.Button(text = 'end game', command = exit)
b1.pack()
b2.pack()
window.mainloop()
