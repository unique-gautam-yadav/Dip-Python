# def fun(a, b):
#     a, b = b, a
#     print("\n\nValue of a -->", a, "\n Value of b --> ", b)


# fun(int(input("Enter Value of a --> ")), int(input("Enter value of b -->")))


# === Reculssion ===


n = int(input("Enter a number -->"))


def rec(n):
    if (n == 0):
        return 1
    else:
        return n * rec(n-1)


print(rec(n))
