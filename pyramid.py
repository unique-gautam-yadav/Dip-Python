n = 5
s = "*"
spc = " "

for i in range(1, n, 1):
    for j in range(n, i+1, -1):
        print(spc, end=' ')
    for j in range(1, i+1, 1):
        print(s, end=' ')
    for j in range(1, i, 1):
        print(s, end=' ')
    for j in range(n, i+1, -1):
        print(spc, end=' ')
    print('')

for i in range(1, n, 1):
    for j in range(1, i+1, 1):
        print(spc, end=' ')
    for j in range(n, i+1, -1):
        print(s, end=' ')
    for j in range(n-1, i+1, -1):
        print(s, end=' ')
    for j in range(1, i+1, 1):
        print(spc, end=' ')
    print('')
