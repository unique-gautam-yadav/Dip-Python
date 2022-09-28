from tkinter import *

root = Tk()
root.geometry("180x120")
root.resizable(FALSE, FALSE)


def fun():
    n = int(num_in.get())
    n1 = 0
    n2 = 1
    count = 1
    fac = [0]
    while nth < n:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        fac.append(nth)
        count = count + 1
    num_out.set(fac)


num_in = StringVar()
num_out = StringVar()


inn = Entry(root, textvariable=num_in).place(x=30, y=10)
btn = Button(root, command=fun, text="Calculate").place(x=50, y=35)
lbl = Label(root, textvariable=num_out).place(x=5, y=95)


root.mainloop()
