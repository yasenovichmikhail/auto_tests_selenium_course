from tkinter import *

def submit():
    print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    listbox.delete(listbox.curselection())

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, 
                      text='submit', 
                      command=submit)
submitButton.pack()

addButton = Button(window, 
                      text='add', 
                      command=add)
addButton.pack()

deleteButton = Button(window, 
                      text='delete', 
                      command=delete)
deleteButton.pack()

window.mainloop()