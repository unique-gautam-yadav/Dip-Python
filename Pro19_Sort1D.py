import numpy as np

arr = np.array([])

n = int(input("Enter no of elements in array ::: "))

for i in range(n):
    v = int(input("Enter a number for " + str(i+1) + " INDEX :: "))
    arr = np.insert(arr, i, v)

print("\n\n\n ::::::: Unsorted Array ::::::: ")
print(arr)

for i in range(arr.size):
    for j in range(i+1, arr.size, 1):
        if (arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]


print("\n\n\n ::::::: Sorted Array ::::::: ")
print(arr)
