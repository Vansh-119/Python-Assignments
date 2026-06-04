import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

arr = np.nan_to_num(arr, nan=0)

print("Array after replacing NaN with 0:")
print(arr)

print("\nTranspose of array:")
print(arr.T)


arr3d = np.arange(24).reshape(2, 3, 4)

print("\nOriginal 3D Array Shape:")
print(arr3d.shape)

moved = np.moveaxis(arr3d, 0, 2)

print("\nShape after moving axis:")
print(moved.shape)


arr2 = np.array([[1, 2, np.nan],
                 [4, np.nan, 6],
                 [7, 8, 9]])

col_mean = np.nanmean(arr2, axis=0)

inds = np.where(np.isnan(arr2))

arr2[inds] = np.take(col_mean, inds[1])

print("\nArray after replacing NaN with column averages:")
print(arr2)


arr4 = np.array([[6, -8, 73],
                 [-10, 5, -2]])

arr4 = np.where(arr4 < 0, 0, arr4)

print("\nNegative values replaced with zero:")
print(arr4)


arr1 = np.array([[3, 4],
                 [5, 6]])

arr2 = np.array([[1, 0],
                 [7, 8]])

average = (arr1 + arr2) / 2

print("\nAverage of arrays:")
print(average)

combined = np.concatenate((arr1.flatten(), arr2.flatten()))

print("\nMean:", np.mean(combined))
print("Median:", np.median(combined))

values, counts = np.unique(combined, return_counts=True)
mode = values[np.argmax(counts)]

print("Mode:", mode)


A = np.array([[1, -2, 3],
              [-1, 3, -1],
              [2, -5, 5]])

B = np.array([9, -6, 17])

solution1 = np.linalg.solve(A, B)

print("\nSolution using linalg.solve():")
print("x =", solution1[0])
print("y =", solution1[1])
print("z =", solution1[2])

A_inv = np.linalg.inv(A)

solution2 = np.dot(A_inv, B)

print("\nSolution using inverse matrix method:")
print("x =", solution2[0])
print("y =", solution2[1])
print("z =", solution2[2])


subjects = ['Python', 'Maths', 'DBMS', 'Java', 'OS']

semester1 = [78, 85, 80, 75, 82]
semester2 = [88, 79, 84, 90, 86]

plt.figure(figsize=(8, 5))

plt.plot(subjects, semester1, marker='o', label='Semester 1')
plt.plot(subjects, semester2, marker='o', label='Semester 2')

plt.title('Semester Result Comparison')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.legend()
plt.grid(True)

plt.show()