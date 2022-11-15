n = int(input("Enter value of x : "))
m = int(input("Enter value of y : "))


def swap(n, m):
    n, m = m, n
    return n, m


n, m = swap(n, m)

print("x :", n)
print("y :", m)
