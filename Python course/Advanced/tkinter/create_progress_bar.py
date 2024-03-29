from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 100
    x = 0
    while x < tasks:
        time.sleep(1)
        bar['value'] +=  1
        x += 1
        percent.set(str(int((x/tasks)*100))+"%")
        window.update_idletasks()

window = Tk()

percent = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()

button = Button(window, text="download", command=start)
button.pack()

window.mainloop()