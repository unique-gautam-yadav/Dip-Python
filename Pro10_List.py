a = ['Gautam', 'Hello', 'asdklj', 34, 21,  42.2]

strings = 0
intger = 0
floats = 0


for i in a:
    if (type(i) == type(2)):
        intger += 1
    elif (type(i) == type('str')):
        strings += 1
    elif (type(i) == type(5.25)):
        floats += 1


print(' Strings =', strings, '\n', 'Integers =',
      intger, '\n', 'Floats =', floats)
