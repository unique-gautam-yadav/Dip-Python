n = int(input("Enter a number "))

i = 2

f = True

while (i < n/2):
    if (n % i == 0):
        f = False
        break
    i += 1

if (f):
    print("Number is prime")
else:
    print("Number is not prime")


r = n
sum = 0

while (r > 0):
    rr = r % 10
    sum = rr + (sum * 10)
    r = int(r / 10)

print(sum)
