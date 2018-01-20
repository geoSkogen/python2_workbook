from tkinter import *

def sel():
    selection = "value = " + str(var.get())
    label.config(text = selection)

root = Tk()
var = DoubleVar()
scale = Scale( root, variable = var)
scale.pack(anchor=CENTER)

button = Button(root, text="check value", command=sel)
button.pack(anchor=CENTER)

label = Label(root)
label.pack()

root.mainloop()
