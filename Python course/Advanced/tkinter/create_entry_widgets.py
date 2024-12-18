from tkinter import *

def submit():
    username = entry.get()
    print(f"Hello {username}")

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black",
              show="*")
# entry.insert(0, "Spongebob")
entry.pack(side=LEFT)

submit_button = Button(window,
                       text="submit",
                       command=submit,
                       font="bold")
delete_button = Button(window,
                       text="delete",
                       command=delete,
                       font="bold")
backspace_button = Button(window,
                       text="backspace",
                       command=backspace,
                       font="bold")
submit_button.pack(side=RIGHT)
delete_button.pack(side=RIGHT)
backspace_button.pack(side=RIGHT)

window.mainloop()