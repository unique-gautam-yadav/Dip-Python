str = input("Enter a string -->")

dict = {}
count = 0


for i in str:
    count += 1
    dict[count] = i


print(dict)
print(count)
