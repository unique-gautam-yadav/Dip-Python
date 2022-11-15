import random
import string

n = int(input("Enter length of captch -->"))

captch = ""

for i in range(n):
    randomLetter = random.choice(string.hexdigits)
    captch += randomLetter


print(captch)