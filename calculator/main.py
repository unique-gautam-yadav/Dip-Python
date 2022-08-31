from tkinter import *

root = Tk()

root.geometry("300x400")
otpt = StringVar()
out = Entry(root, textvariable=otpt,width=46,
            state="readonly").place(x=10, y=10)

root.mainloop()
