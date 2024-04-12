from tkinter import *

def click():
    print("You clicked the button!")

window = Tk()

button = Button(window,
                text='Click me',
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                state=ACTIVE)
button.pack()

window.mainloop()