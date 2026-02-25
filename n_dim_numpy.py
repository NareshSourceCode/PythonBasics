import numpy as np
# Create a 3x3 array with random integers
array_3x3 = np.random.randint(0, 100, size=(3, 3))

print(array_3x3)
# Create a 3x3 numpy array
array_3x3 = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])
print("Original 3x3 array:")
print(array_3x3)
slice_2x2 = array_3x3[0:2, 0:2]
print("Slice of 2x2 array:")
print(slice_2x2)
slice_1x3 = array_3x3[1:2, :]
print("Slice of 1x3 array:")
print(slice_1x3)
slice_2x3 = array_3x3[1:3, 0:3]
print("Slice of 2x3 array:")
print(slice_2x3)