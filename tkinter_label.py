from tkinter import *

root = Tk()

var = StringVar()
label = Label(root, textvariable=var, relief=RAISED)

var.set("Hello Python!")
label.pack()
root.mainloop()
