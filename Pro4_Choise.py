n = float(input("Enter A Number -->"))
m = float(input("Enter another number -->"))

c = 5
while(c > 0):
    print("Press 1 to add")
    print("Press 2 to sub")
    print("Press 3 to mul")
    print("Press 4 to div")
    print("Press 0 to exit")
    c = int(input("Enter your Choise -->"))
    if c is 0:
        print()
    elif c is 1:
        print(n + m)
    elif c is 2:
        print(n - m)
    elif c is 3:
        print(n * m)
    elif c is 4:
        print(n / m)
    else:
        print("Invalid Choise")
