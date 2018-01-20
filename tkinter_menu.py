from tkinter import *
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="does nothing")
    button.pack

root = Tk()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Window", command=donothing)
filemenu.add_command(label="New File", command=donothing)
filemenu.add_command(label="New Damage", command=donothing)
filemenu.add_command(label="Open File", command=donothing)
filemenu.add_command(label="Open Folder", command=donothing)
filemenu.add_command(label="Release Wolves", command=donothing)
filemenu.add_command(label="Reopen Last Item", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Settings", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Scalps", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Close Tab", command=donothing)
filemenu.add_command(label="Close Window", command=donothing)
filemenu.add_command(label="Jump out the Window", command=donothing)
filemenu.add_command(label="...Like a Boss", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=donothing)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_command(label="Raid", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Bury", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)

viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Toggle Full Screen", command=donothing)
viewmenu.add_command(label="Toggle Menu Bar", command=donothing)
viewmenu.add_separator()
viewmenu.add_command(label="Googgle Yourself", command=donothing)
viewmenu.add_separator()
viewmenu.add_command(label="Toggle Tree View", command=donothing)

menubar.add_cascade(label="View", menu=viewmenu)

root.config(menu=menubar)
root.mainloop()
