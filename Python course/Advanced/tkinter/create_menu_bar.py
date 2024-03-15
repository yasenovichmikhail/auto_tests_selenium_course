from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(title='Open file',
                                          filetypes=(("text files", "*.txt"),
                                          ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

def  saveFile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\Desktop',
                                    title='Save file',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ('Text file',  '.txt'),
                                        ('HTML file',  '.html'),
                                        ('All files',  '.*')
                                    ])
    if file is None:
        return
    
def cut():
    print("You cut some text")

def copy():
    print("You copied some text")

def paste():
    print("You pasted some text")

window = Tk()

openImage = PhotoImage(file="open.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, 
                tearoff=0)
menubar.add_cascade(label="File", 
                    menu=fileMenu)
fileMenu.add_command(label="Open", 
                     command=openFile, 
                     image=openImage, 
                     compound="left")
fileMenu.add_command(label="Save", 
                     command=saveFile, 
                     image=saveImage, 
                     compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", 
                     command=quit, 
                     image=exitImage, 
                     compound="left")

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", 
                    menu=editMenu)
editMenu.add_command(label="Cut", 
                     command=cut)
editMenu.add_command(label="Copy", 
                     command=copy)
editMenu.add_command(label="Paste", 
                     command=paste)

window.mainloop()