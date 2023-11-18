from tkinter import *

def printSomething():
    label.config(text="Hey, what's up bro? I am doing something very interesting.")

root = Tk()
button = Button(root, text="Print Me", command=printSomething)
button.pack()

label = Label(root, text="")
label.pack()

root.mainloop()