from tkinter import *

import tkinter

top = Tk()

Lb1 = Listbox(top, selectmode="MULTIPLE")
Lb1.insert(1, "Python")
Lb1.insert(2, "PHP")
Lb1.insert(3, "Ruby")
Lb1.insert(4, "C#")
Lb1.insert(5, "JavaScript")

Lb1.pack()
top.mainloop()
