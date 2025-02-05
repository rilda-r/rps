#ROCK PAPER SCISSORS


import tkinter as tk
import random
from tkhtmlview import HTMLLabel

u=0
c=0
def gaming():
    global u,c
    user = user_choice.get()
    # print('user:',user)

    choice = ['rock','paper','scissors']
    comp_choice = random.choice(choice)
    # print('comp:',comp_choice)
     
    if user.lower() in choice:
        if comp_choice == user.lower():
            l.configure(text='no one scored')
            # print('no one scored')
            

        elif (comp_choice == 'rock' and user.lower() == 'paper') or (comp_choice == 'paper' and user.lower() == 'scissors') or (comp_choice == 'scissors' and user.lower() == 'rock'):
            l.config(text='u score')
            # print('u score')
            u+=1
            
        elif (comp_choice == 'rock' and user.lower() == 'scissors') or (comp_choice == 'paper' and user.lower() == 'rock') or (comp_choice == 'scissors' and user.lower() == 'paper'):
            l.configure(text='comp scores')
            # print('comp scores')
            c+=1
            
    else:
        l.configure(text='wrong input. Change the input!')
        # print('wrong input!')
       
    
def stop():
    print('comp scored', c,'times')
    print('you scored',u,'times')
    l.config(text=f'comp scored {c} times AND you scored {u} times')    
    
    if c>u:
        print('COMP TAKES THE WIN')
        l2=tk.Label(text='COMP TAKES THE WIN', bg='lightblue')    
    elif c<u:
        print('YOU TAKE THE WIN')
        l2=tk.Label(text='YOU TAKE THE WIN', bg='lightpink')    
    else:
        print('ITS A DRAW')
        l2=tk.Label(text='ITS A DRAW', bg='lightgrey')    
    l2.pack(side=tk.LEFT)
    

window = tk.Tk()
window.title('rock paper scissors')
window.geometry('1270x680')

line = HTMLLabel(window, html = "\
                 <h1 style='color:red;'><b>hi! ITs the rock paper scissors game!</b></h1>\
                 <img src='https://i.ytimg.com/vi/Z13kiomZvak/maxresdefault.jpg'>\
                 <rock>Give your input rock/paper/scissors</h1>\
                 <h4>click 'stop' to get the results and 'end game' to quit</h4>\
                 ")
line.pack(fill='both',expand='true')


l1 = tk.Label(text='user-choice',font=("arial", 20), bg='lightgreen')
l1.pack()

user_choice = tk.StringVar()
e1 = tk.Entry(textvariable = user_choice)
e1.pack()

l=tk.Label(window,text='heyyo')  
l.pack() 

b1 = tk.Button(text = 'result', command = gaming)
b1.pack()

b3 = tk.Button(text = 'end game', command = exit)
b3.pack(side=tk.RIGHT)

b2 = tk.Button(text = 'stop', command = stop)
b2.pack(side=tk.RIGHT, padx=10, pady=5)

window.mainloop()
