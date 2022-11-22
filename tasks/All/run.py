from tkinter import *


class RunTheProgram:

    def __init__(self, program):
        self.program = program

    def run(self):
        root = Tk()
        root.geometry("500x500")
        if (self.program.__contains__("2.")):
            Label(root, text="Hello World !!").place(x=100, y=200)
        elif (self.program.__contains__("3.")):

            val = StringVar()
            v = StringVar()

            def exe():
                v.set(val.get())

            Entry(root, textvariable=val).place(x=50, y=150)
            Button(root, text="Submit", command=exe).place(x=50, y=200)
            Label(root, textvariable=v).place(x=50, y=250)

        elif (self.program.__contains__("4.")):
            n1 = IntVar()
            n2 = IntVar()
            ch = StringVar()
            out = StringVar()
            out.set("OUTPUT")

            def calcu():
                n = n1.get()
                m = n2.get()
                c = ch.get()
                res = str(0)
                if c == "1":
                    res = str(n + m)
                elif c == "2":
                    res = str(n - m)
                elif c == "3":
                    res = str(n * m)
                elif c == "4":
                    res = str(n / m)
                else:
                    res = "OUTPUT"

                out.set(res)

            Label(root, text="First Number").place(x=0, y=0)
            Entry(root, textvariable=n1).place(x=150, y=0)
            Label(root, text="Second Number").place(x=0, y=25)
            Entry(root, textvariable=n2).place(x=150, y=25)
            Label(root, text="Select 1 to Add\nSelect 2 to Sub\nSelect 3 to Mul\nSelect 4 to Div").place(
                x=10, y=45)
            OptionMenu(root, ch, *["1", "2", "3", "4"]).place(x=10, y=120)
            Button(root, text="CALCULATE", command=calcu).place(x=10, y=160)
            Label(root, textvariable=out).place(x=10, y=190)

        elif (self.program.__contains__("5.")):
            n = IntVar()
            out = StringVar()
            out.set("OUTPUT")

            def fun():
                outt = ""
                for i in range(n.get()):
                    outt = outt + " " + str(i)
                out.set(outt)
            Label(root, text="Enter Range").place(x=5, y=2)
            Entry(root, textvariable=n).place(x=155, y=2)
            Button(root, text="Print", command=fun).place(x=5, y=30)
            Label(root, textvariable=out).place(x=10, y=65)

        elif (self.program.__contains__("6.")):
            inpt = StringVar()
            out = StringVar()
            out.set("Output Here")

            def fun():
                got = inpt.get()
                if got == "Int (5)":
                    out.set(str(str(type(5))))
                elif got == "Float (4.5)":
                    out.set(str(type(4.5)))
                elif got == "String ('Gautam')":
                    out.set(str(type("Gautam")))
                elif got == "List [3, 5]":
                    out.set(str(type([3, 5])))
                elif got == "Touple (4, 5)":
                    out.set(str(type((4, 5))))
                else:
                    out.set("Output Here")

            Label(root, text="Select Data Type --> ").place(x=5, y=2)
            OptionMenu(root, inpt, *["Int (5)", "Float (4.5)",
                       "String ('Gautam')", "List [3, 5]", "Touple (4, 5)"]).place(x=150, y=2)
            Button(root, text="Execute", command=fun).place(x=5, y=25)
            Label(root, textvariable=out).place(x=10, y=55)

        elif (self.program.__contains__("7.")):
            n = IntVar()
            out = StringVar()
            out.set("Output Here")

            def fun():
                got = n.get()
                if got % 2 == 0:
                    out.set("Number is Even.")
                elif got % 2 != 0:
                    out.set("Number is Odd.")

            Label(root, text="Enter a Number").place(x=5, y=2)
            Entry(root, textvariable=n).place(x=150, y=2)
            Button(root, text="Execute", command=fun).place(x=5, y=25)
            Label(root, textvariable=out).place(x=10, y=55)

        elif (self.program.__contains__("8.")):
            n = IntVar()
            out = StringVar()
            out.set("OUTPUT")

            def fun():
                outt = ""
                for i in range(n.get()):
                    if (i == 2):
                        continue
                    else:
                        outt = outt + " " + str(i)

                out.set(outt)

            Label(root, text="Enter Range").place(x=5, y=2)
            Entry(root, textvariable=n).place(x=155, y=2)
            Button(root, text="Print", command=fun).place(x=5, y=30)
            Label(root, textvariable=out).place(x=10, y=65)

        elif (self.program.__contains__("9.")):
            l = IntVar()
            b = IntVar()
            h = IntVar()
            out = StringVar()
            out.set("Output Here!!")

            def fun():
                le = l.get()
                br = b.get()
                hi = h.get()
                out.set("Area = " + str((br*hi)/2) +
                        " ::::: Parameter = " + str(br + hi + le))

            Label(root, text="Enter Length :: ").place(x=5, y=2)
            Entry(root, textvariable=l).place(x=150, y=2)
            Label(root, text="Enter Breath :: ").place(x=5, y=25)
            Entry(root, textvariable=b).place(x=150, y=25)
            Label(root, text="Enter Height :: ").place(x=5, y=50)
            Entry(root, textvariable=h).place(x=150, y=50)
            Button(root, text="Execute", command=fun).place(x=5, y=80)
            Label(root, textvariable=out).place(x=10, y=105)

        elif (self.program.__contains__("10.")):
            nums = StringVar()
            out = StringVar()
            out.set("Output Here!!")

            def fun():
                nms = nums.get()
                out.set(str(nms.split(sep=",")))

            Label(root, text="Enter Values by Saperation by commas => 5,2,3").place(
                x=5, y=2)
            Entry(root, textvariable=nums).place(x=300, y=2)
            Button(root, text="Execute", command=fun).place(x=5, y=25)
            Label(root, textvariable=out).place(x=10, y=55)
        root.mainloop()
