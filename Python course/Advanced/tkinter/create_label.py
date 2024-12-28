from tkinter import *

window = Tk()

label = Label(window, 
              text='Hello World', 
              font=('Arial', 40, 'bold'), 
              fg='green', 
              bg='blue',
              padx=20,
              pady=20,
              compound='bottom')

label.pack()

window.mainloop()