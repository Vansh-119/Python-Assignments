import numpy as np

arr = np.array([[6, -8, 73, -110],
                [np.nan, -8, 0, 94]])

arr = np.nan_to_num(arr, nan=0)

print("Array after replacing NaN with 0:")
print(arr)

transpose_arr = arr.T

print("\nTranspose of array:")
print(transpose_arr)


arr3d = np.arange(24).reshape(2, 3, 4)

print("\nOriginal 3D Array:")
print(arr3d)

moved = np.moveaxis(arr3d, 0, 2)

print("\n3D Array after moving axis:")
print(moved)


arr2 = np.array([[1, 2, np.nan],
                 [4, np.nan, 6],
                 [7, 8, 9]])

col_avg = np.nanmean(arr2, axis=0)

inds = np.where(np.isnan(arr2))

arr2[inds] = np.take(col_avg, inds[1])

print("\nArray after replacing NaN with column averages:")
print(arr2)


arr3 = np.array([10, -5, 20, -8, 30])

arr3[arr3 < 0] = 0

print("\nArray after replacing negative values with 0:")
print(arr3)