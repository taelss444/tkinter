from tkinter import *


window = Tk()
window.title('Кликер')
window.geometry('300x200')
window.resizable(width=False, height=False)
window['bg'] = 'black'

count = 0


def click():
    global count
    count += 1
    clicked.configure(text=count)


clicked = Label(window, text='0', fg='#FFFF99', font=('Comic Sans MS', 20, 'italic'), bg='black')
clicked.pack()

btn = Button(window,
    text="Кликни",
    font=("Comic Sans MS", 20, 'italic'),
    background='#CCCCFF',
    foreground='#1CAC78',
    activebackground='#1CAC78',
    activeforeground='#CCCCFF',
    command=click)
btn.pack()


window.mainloop()
