a = ['Gautam', 'Hello', 'asdklj', 34, 21,  42.2]
inn = 2
s = 'ge'
f = 3.3


inn = type(inn)
s = type(s)
f = type(f)


strings = 0
intger = 0
floats = 0


for i in a:
    if (type(i) == inn):
        intger += 1
    elif (type(i) == s):
        strings += 1
    elif (type(i) == f):
        floats += 1


print('Strings =', strings, 'integers =', intger, 'floats =', floats)
