import numpy as np
# Part A
a = np.loadtxt('values.txt')
b = a.reshape(2, 4, 3)
#print('a =', a)
#print('b =', b)

# Part B

#print('Block 0:\n', b[0, :, :])

#print('Second rows:\n', b[:, 1, :])

#print('First columns:\n', b[:, :, 0])

#print('Block 1 with reversed rows :\n', b[1, ::-1, :])

# Part C
c = np.ma.masked_less(b, 50)
d = np.ma.masked_inside(b, 50, 70)
e = np.ma.masked_greater_equal(b, 75)



# Part D

rowsum = b.sum(axis=2)
max_row = np.argmax(rowsum)