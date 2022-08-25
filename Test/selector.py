from ast import pattern
from tkinter import *


root = Tk()

otpt = StringVar()


def getRevTri(par):
    n = int(par)
    s = '*'
    spc = ' '
    ptrn = ''


def getTriangle(par):
    n = int(par)
    s = '*'
    spc = ' '
    ptrn = ''
    for i in range(1, n, 1):
        for j in range(n, i+1, -1):
            # print(spc, end=' ')
            ptrn += spc + ' '
        for j in range(1, i+1, 1):
            # print(s, end=' ')
            ptrn += s + ' '
        for j in range(1, i, 1):
            # print(s, end=' ')
            ptrn += s + ' '
        for j in range(n, i+1, -1):
            # print(spc, end=' ')
            ptrn += spc + ' '
        # print('')
        ptrn += '\n'
    otpt.set(ptrn)


def getDaimod(par):
    n = int(par)
    s = '*'
    spc = ' '
    ptrn = ''
    for i in range(1, n, 1):
        for j in range(n, i+1, -1):
            # print(spc, end=' ')
            ptrn += spc + ' '
        for j in range(1, i+1, 1):
            # print(s, end=' ')
            ptrn += s + ' '
        for j in range(1, i, 1):
            # print(s, end=' ')
            ptrn += s + ' '
        for j in range(n, i+1, -1):
            # print(spc, end=' ')
            ptrn += spc + ' '
        # print('')
        ptrn += '\n'

    for i in range(1, n, 1):
        for j in range(1, i+1, 1):
            print(spc, end=' ')
            ptrn += spc + ' '
        for j in range(n, i+1, -1):
            print(s, end=' ')
            ptrn += s + ' '
        for j in range(n-1, i+1, -1):
            print(s, end=' ')
            ptrn += s + ' '
        for j in range(1, i+1, 1):
            print(spc, end=' ')
            ptrn += spc + ' '
        print('')
        ptrn += '\n'
    otpt.set(ptrn)


def operate():
    if (shape.get() == 1):
        getDaimod(inpt.get())
    elif (shape.get() == 2):
        getTriangle(inpt.get())
    elif (shape.get() == 3):
        getRevTri(inpt.get())


root.geometry("300x400")

inpt = StringVar()

lbl = Label(root, text="No of Rows").place(x=30, y=10)
inpt_fld = Entry(root, textvariable=inpt).place(x=120, y=10)

shape = IntVar()
Radiobutton(root, text="Daimond",  variable=shape,
            value=1).place(x=50, y=40)
Radiobutton(root, text="Triangle", variable=shape,
            value=2).place(x=190, y=40)
Radiobutton(root, text="Resv Triangle",  variable=shape,
            value=3).place(x=50, y=65)
Radiobutton(root, text="Type 4",   variable=shape,
            value=4).place(x=190, y=65)

Button(root, text="Print", command=operate).place(x=145, y=85)


Label(root, textvariable=otpt).place(x=50, y=150)

root.mainloop()
