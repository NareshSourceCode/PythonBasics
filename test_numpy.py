import numpy as np

#Method declaration
def test_numpy_array(val ):
    a = np.array([1, 2, 3]) 
    a=a*val
    print(a)
#method call
test_numpy_array(10)

#Adding two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = arr1 + arr2
print(result)

#Subtracting two arrays
result = arr1 - arr2
print(result)

#Multiplying two arrays
result = arr1 * arr2
print(result)


