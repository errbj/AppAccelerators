# Exercise one
# Name: Eduardo R Rodrigues de Brito Junior
# Course: Applications of Accelerators

import numpy as np

# Function definitions
def Add2plus2():
    s = 2 + 2
    return s

def MultiplyArray(a,b):
    #This function multiplies two arrays using numpy dot
    c = a.dot(b);
    return c

def MultiplyArrayManually(a,b):
    #This function only multiplies two 3x3 arrays manually
    lin_a = np.size(a,0)
    col_a = np.size(a,1)
    lin_b = np.size(b,0)
    col_b = np.size(b,1)
    if lin_a != 3:
        print('Size different from 3, use function MultiplyArray')
        return 0
    if col_a != 3:
        print('Size different from 3, use function MultiplyArray')
        return 0
    if lin_b != 3:
        print('Size different from 3, use function MultiplyArray')
        return 0
    if col_b != 3:
        print('Size different from 3, use function MultiplyArray')
        return 0
    c = np.zeros((3,3))
    for ik in range(3):
        for jk in range(3):
            for wk in range(3):
                c[ik][jk] = c[ik][jk] + a[ik][wk]*b[wk][jk]
    return c
            
    
# Use of function Add2plus2
a = Add2plus2()
print('Result from Add2plus2 = ',a)

# Use of function MultiplyArray
v = np.random.random((3,3))
y = np.random.random((3,3))
print('\nMatrix 1\n',v)
print('\nMatrix 2\n',y)
x = MultiplyArray(v,y)
print('\nResult from MultiplyArray = \n',x)

# Use of function MultiplyArrayManually
w = MultiplyArrayManually(v,y)
print('\nResult from MultiplyArrayManually = \n',w)