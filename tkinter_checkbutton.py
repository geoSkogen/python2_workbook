from tkinter import *
import tkinter

top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "JellyFishers", variable = CheckVar1, onvalue = 1, offvalue = 0, height = 5, width = 45)
C2 = Checkbutton(top, text = "BubbleBlowers", variable = CheckVar2, onvalue = 1, offvalue = 0, height = 5, width = 45)
C1.pack()
C2.pack()
top.mainloop()
