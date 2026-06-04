import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6],
                 [7, 8, 9]])

combined = np.vstack((arr1, arr2))
print("Combined Array:\n", combined)

flat = arr2.flatten()
print("Flattened Array:", flat)

rev = arr1[::-1]
print("Reversed Array:", rev)

arr = np.array([[10, 20, 30],
                [5, 15, 25]])

print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Shape:", arr.shape)

print("All elements:")
for i in arr:
    for j in i:
        print(j, end=" ")
print()

print("Specific element [1][2]:", arr[1][2])

sum_val = 0
for i in arr:
    for j in i:
        sum_val += j
print("Sum using loop:", sum_val)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)

arr3d = np.array([[[1, 2], [3, 4]],
                  [[5, 6], [7, 8]]])

print("3D Iteration (for loop):")
for i in arr3d:
    for j in i:
        for k in j:
            print(k, end=" ")
print()

print("3D Iteration (nditer):")
for x in np.nditer(arr3d):
    print(x, end=" ")
print()

arrA = np.array([[1, 2, 3],
                 [4, 5, 6]])

arrB = np.array([[7, 8, 9],
                 [10, 11, 12]])

combined2 = np.concatenate((arrA, arrB))

mean_val = np.mean(combined2)
median_val = np.median(combined2)

values, counts = np.unique(combined2, return_counts=True)
mode_val = values[np.argmax(counts)]

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)