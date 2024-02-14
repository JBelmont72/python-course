'''

https://www.youtube.com/watch?v=GB9ByFAIAH4

'''
import numpy as np

a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# Get Dimension
a.ndim

# Get Shape
b.shape
# Get Type
a.dtype


a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)

# Get a specific element [r, c]
print(a[1, 5])

# Get a specific row 
print(a[0, :])
# Get a specific column  
print(a[:, 2])  # output  [ 3 10]

# Getting a little more fancy [startindex:endindex:stepsize]
print(a[0, 1:-1:2]) # 0 index, start at index one and go all the way to the last but not including the last  in steps of 2
#       [2 4 6]
print(a[1,0:   :2]) # index('row') 1, start at column 0 and go to the end by 2s 
#       [ 8 10 12 14]

a[1,5] = 20

# a[:,2] = [1,2]
# print(a)
# a[1,5] = 20
print('')
a[1 :,2] = [20] # this takes row 1 and changes column index 2
print(a)

b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
print('new array')
print(b[0:1,1])
