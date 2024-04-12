# All the input arrays must have same number of dimensions

import numpy as np

arr1 = np.array([1, 2])

print(arr1.shape)  # 👉️ (2,)

arr2 = np.array([
    [3, 4],
    [5, 6]
])

print(arr2.shape)  # 👉️ (2, 2)

arr3 = np.column_stack((arr1, arr2))

# [[1 3 4]
#  [2 5 6]]
print(arr3)