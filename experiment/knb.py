from tkinter import *
from random import *


window = Tk()
window.title('Камень/Ножницы/Бумага')
window.geometry('620x720')
window.resizable(width=False, height=False)
window['bg'] = 'black'


def click():
    all = ['Камень','Ножницы', 'Бумага']
    new_all = choice(all)
    labelText.configure(text=new_all)


labelText = Label(window, text='', fg='white', font=('Comic Sans MS', 20, 'italic'),bg='black')
labelText.place(y=240, x=240)

stone = Button(window,
    text="Камень",
    font=("Comic Sans MS", 20, 'italic'),
    background='#FFDB58',
    foreground='#FD7C6E',
    activebackground='#FD7C6E',
    activeforeground='#FFDB58',
    command=click)
stone.place(x=50, y=300)

scissors = Button(window,
    text="Ножницы",
    font=("Comic Sans MS", 20, 'italic'),
    background='#FAE7B5',
    foreground='#755D9A',
    activebackground='#755D9A',
    activeforeground='#FAE7B5',
    command=click)
scissors.place(x=235, y=300)

paper = Button(window,
    text="Бумага",
    font=("Comic Sans MS", 20, 'italic'),
    background='#ADDFAD',
    foreground='#42AAFF',
    activebackground='#42AAFF',
    activeforeground='#ADDFAD',
    command=click)
paper.place(x=450, y=300)

window.mainloop()