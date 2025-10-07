# numpy --> numerical python
#  
# NumPy (Numerical Python) is a fundamental Python library for numerical and scientific computing.
# It provides powerful data structures (mainly ndarray) for handling large datasets efficiently.
# Built on C and Fortran, so operations are fast and memory-efficient compared to normal Python lists.
import numpy as np
import time

start_time = time.time()
list1 = [i for i in range(10000)]
# print(list1)
end_time = time.time()
print(end_time-start_time)



# using numpy
start_time = time.time()
np1 = np.arange(0,10000)
# print(np1)
end_time = time.time()
print(end_time-start_time)



# Arrays Basics
# Create arrays using different functions:

a = np.array([1, 2, 3]) # 1D array
print(a)
print(type(a))  #<class 'numpy.ndarray'>  --> it is different from python list

b = np.array([[1,2,3],[4,5,6]]) # 2D array
print(b)

c = np.zeros((2,3)) # zeros (2 rows and 3 cols filled with 0's)
print(c)

d = np.ones((3,3)) # ones (3 rows and 3 cols filled with 1's)
print(d)   

e = np.eye(3) # identity matrix
print(e)

f = np.arange(0, 10, 2) # range array o/p: [0 2 4 6 8]
print(f)

g = np.linspace(0, 1, 5) # evenly spaced (from 0 to 1, generates 5 numbers with equal space, i.e divides 5 equal parts from 0 to 1)
print(g)

# Attributes
# a.shape, a.ndim, a.size, a.dtype (datatype), a.itemsize (gives element space inside matrix)

print("-------Attributes-------")
np1 = np.array([[1,2,3],[4,5,6]])
print(np1.shape) #o/p: (2,3) --> 2 rows and 3 cols
print(np1.ndim) #o/p: 2-> 2 dimentional array
print(np1.size) #o/p: 6 --> gives no of elements in array
print(np1.dtype) #o/p: int64 --> data type is int with 64 bits
print(np1.itemsize) #o/p: 8 --> gives element space inside matrix (8 bytes)

# Indexing & Slicing
# Index arrays using standard slicing, boolean masking:

print("------Indexing & Slicing------")
arr = np.array([10,20,30,40,50])
print(arr)
print(arr[0])
print(arr[-1])
print(arr[1:4]) 
print(arr[::-1])

mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat)
print(mat[0,0]) #  mat[row,col] o/p: 1 (gives 1st row)

print(mat[:,1])

# : means all rows
# 1 means second column
# So it picks values of all rows from column index 1 → [2, 5, 8]

print(mat[1,:]) #1 means 2nd row from all cols i.e [4, 5, 6]

print(mat[0:2,1:3])

# 0:2 → take rows from 0 up to (but not including) 2 → rows [0, 1]
# 1:3 → take columns from 1 up to (but not including) 3 → columns [1, 2]
# Sub-matrix formed:
# [[2 3]
#  [5 6]]

arr = np.array([1,2,3,4,5])
print(arr)
print(arr[arr > 3]) # [4,5]


# Array Operations
# Perform elementwise operations and broadcasting:

print("------Array operations------")

a = np.array([1,2,3])
b = np.array([4,5,6])
print(a + b) # [5,7,9]
print(a * b) # [4,10,18]
print(a ** 2) # [1,4,9]

a = np.array([[1],[2],[3]])
print(a)
b = np.array([10,20,30])
print(b)

print(a+b) #broadcasting

# Aggregations
# Aggregation functions:

print("-------Aggregate functions-------")

arr = np.array([[1,2,3],[4,5,6]])
print(arr.sum())  #gives sum of all elements in array
print(arr.mean())
print(arr.min())
print(arr.max())
print(arr.std()) # gives standard deviation value using formula (sqrt(x-mean)^2)

print(arr.var()) # gives variance value 
# Variance = square of std.
# 1.7078² = 2.9166...
# Output: 2.9166666666666665

print(arr.sum(axis=0))
# axis=0 → sum column-wise (down each column).

# col1: 1+4 = 5
# col2: 2+5 = 7
# col3: 3+6 = 9
# Output: [5 7 9]

print(arr.sum(axis=1))
# axis=1 → sum row-wise (across each row).

# row1: 1+2+3 = 6
# row2: 4+5+6 = 15
# Output: [ 6 15 ]

# Reshaping & Stacking
# Reshape arrays and stack them:
print("--------Reshaping and Stacking--------")

# Create array from 0 to 11
arr1 = np.arange(12)
print(arr1)

# Reshape to 3x4
reshape = arr1.reshape(3,4) # 12 numbers can be reshaped to 3 rows and 4 cols
print(reshape)

# Flatten (convert to 1D)
flattened = reshape.flatten()
print(flattened)

# Transpose
transposed = reshape.T
print(transposed)

# Define 1D arrays
a = np.array([1,2,3])
b = np.array([4,5,6])

# Vertical stack
v_stacked = np.vstack([a,b])
print(v_stacked)

# o/p: 
# [[1 2 3]
#  [4 5 6]]

# Horizontal stack
h_stacked = np.hstack([a,b])
print(h_stacked)

# o/p:
# [1 2 3 4 5 6]

# Column stack
col_stacked = np.column_stack((a,b))
print(col_stacked)

# o/p:
# [[1 4]
#  [2 5]
#  [3 6]]

# Random Numbers
# Random number generation:

print("-------Random Numbers-------")
print(np.random.rand(3,3)) #3x3 array (only positive numbers from 0 to 1)
print(np.random.randn(3,3)) # Values can be negative or positive.
print(np.random.randint(1,10,5)) # np.random.randint(low, high, size) generates 5 numbers from 1 to 10 
print(np.random.choice([1,2,3])) #Randomly selects one element (or multiple) from a given array.

print(np.random.seed(42)) #does not change random values for below matrix
print(np.random.rand(3,3)) 




# Linear Algebra
# Matrix operations:

print("------Linear Algebra-------")
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.dot(A,B))
print(A @ B)
print(np.linalg.inv(A))
print(np.linalg.det(A))
print(np.linalg.eig(A))


# Useful Functions
# Extra useful tools:

print("------Extra usefull function-------")

print(np.unique([1,2,2,3]))
print(np.sort([3,1,2]))
print(np.argsort([3,1,2])) #It doesn’t sort the array directly, it tells you how to reorder the elements. 
# sorted order is [1,2,3] -->o/p is [1,2,0] (indeces of original array)
# i.e
# 1 is at 1st index
# 2 is at 2nd index
# 3 is at 0th index 

print( np.where(np.array([1,2,3,4]) > 2))

# np.where(condition) returns the indices where the condition is True.
# So here:
# 3 is at index 2
# 4 is at index 3
# Output:(array([2, 3]),) i.e elements greater than 2 are found at positions 2 and 3.

print(np.clip([1,5,7,9], 2, 8)) # np.clip(arr, min, max) 

# It forces all values to stay within [2, 8].
# If a value is smaller than 2, it becomes 2.
# If a value is larger than 8, it becomes 8.

print(np.isnan(np.nan))
print(np.isfinite([1, np.inf, np.nan]))