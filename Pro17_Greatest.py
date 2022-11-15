from tkinter import *

root = Tk()
root.geometry("400x200")


inputs = StringVar()
res = IntVar()


def fun():
    inn = inputs.get()
    elems = inn.split(",")
    intels = []
    for el in elems:
        intels.append(int(el))
    intels.sort()
    res.set(intels[-1])


Label(root, text="Enter values by saperation commas. e.g. --> x,y,z").place(x=25, y=0)
Entry(root, textvariable=inputs).place(x=20, y=20)
Entry(root, textvariable=res).place(x=20, y=50)

Button(root, text="Calculate", command=fun).place(x=60, y=100)


root.mainloop()
