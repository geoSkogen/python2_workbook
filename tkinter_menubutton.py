from tkinter import *
import tkinter

top = Tk()

mb = Menubutton(top, text="neighbors", relief=RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff=0)
mb["menu"] = mb.menu

jellyVar = IntVar()
bubbleVar = IntVar()

mb.menu.add_checkbutton(label="jellyfishers", variable=jellyVar)
mb.menu.add_checkbutton(label="bubbleblowers", variable=bubbleVar)

mb.pack()
top.mainloop()
