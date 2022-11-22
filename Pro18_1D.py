import numpy as np

arr = np.array([1, 2, 3])

print(arr)
print("First Element :", arr[0])

print("\n\n\n #####Iteration of array##### \n\n\n")
for i in range(3):
    print(i+1, "Element :", arr[i])
print(type(arr))
