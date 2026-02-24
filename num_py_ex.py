import numpy as np

rng = np.random.default_rng(seed=0)
# Create a 3x3 matrix of random integers between 1 and 100
matrix = rng.integers(1, 101, size=(3, 3))
print(matrix.T)

print(matrix[0:])
print(matrix[:,:])
# a = np.random.randint(5,100,size=(5, 5))
# b= np.random.randint(5,100,size=(5, 5))

# print(a)
# print(b)
# print(a-b) 


 