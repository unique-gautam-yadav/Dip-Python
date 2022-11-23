n = int(input("Enter a number ::: "))


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print("Factorial of given Number is ", fact(n=n))
