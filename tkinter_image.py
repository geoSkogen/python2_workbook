from tkinter import *
from tkinter import messagebox

top = Tk()

C = Canvas(top, bg="grey", height=206, width=290)

filename = PhotoImage(file = "calamity_jane.gif")
image = C.create_image(290, 5, anchor = NE, image = filename)
C.pack()
top.mainloop()
