import numpy as np

l = []
rows = int(input("Enter no of rows ::: "))
cols = int(input("Enter no of columns ::: "))

for r in range(rows):
    for c in range(cols):
        val = int(
            input("Enter element at [" + str(r) + "] [" + str(c) + "] ::: "))
        l.append(val)

arr = np.array(l).reshape(rows, cols)
print("\n\n\n", arr)
