import numpy as np

arr1d = np.array([1, 2, 3, 4, 5, 6])
arr2d = arr1d.reshape(2, 3)

print(arr2d.shape)
print(arr2d.ndim)
print(arr2d.dtype)
print(arr2d.itemsize)

arr_9 = np.full((3, 3), 9)
print(arr_9)

arr_lin = np.linspace(25, 125, 10)
print(arr_lin)

py_list = [10, 20, 30, 40]
arr_from_list = np.array(py_list)
print(arr_from_list)

rev_arr = arr1d[::-1]
print(rev_arr)

arr_3d = np.arange(48).reshape(4, 4, 3)
print(arr_3d[1, 0, -1])

arr_4x4 = np.arange(1, 17).reshape(4, 4)
print(arr_4x4[1::2, ::2])

print(arr_3d[1, :2, :2])

arr_replace = np.array([[23, 56, 78, 93], [71, 82, 13, 24]])
for i in range(arr_replace.shape[0]):
    for j in range(arr_replace.shape[1]):
        if arr_replace[i][j] % 2 != 0:
            arr_replace[i][j] = -1
print(arr_replace)

arr_nonzero = np.array([1, 0, 2, 0, 3, 0, 4])
print(np.nonzero(arr_nonzero))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)

arr1 = np.array([15, 20, 25])
arr2 = np.array([10, 40, 37])
print(np.dot(arr1, arr2))