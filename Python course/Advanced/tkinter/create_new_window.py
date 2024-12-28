from tkinter import *

def create_window():
    new_window = Tk()     #Tk() = new independent window
                          #Toplevel() = new window 'on top' of other windows
    old_window.destroy()

old_window  = Tk()

Button(old_window, text="createnew window", command=create_window).pack()

old_window.mainloop()