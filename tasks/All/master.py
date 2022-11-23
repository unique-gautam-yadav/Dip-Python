from tkinter import *

from run import RunTheProgram

root = Tk()
root.geometry("300x300")

entries = ["2. Hello", "3. Input", "4. Choise", "5. Range",
           "6. Type", "7. Odd and Even", "8. Continue", "9. Area of Triangle", "10. List"]

val = StringVar()


def fun():
    value = val.get()
    obj = RunTheProgram(value)
    root.destroy()
    obj.run()


menu = OptionMenu(root, val, *entries).place(x=30, y=30)

btn = Button(root, text="Submit", command=fun).place(x=50, y=100)

root.mainloop()
