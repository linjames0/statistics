# calculate the cross entropy between sets of two distributions
import numpy as np
import matplotlib.pyplot as plt

def cross_entropy(p, q):
    # calculate the cross entropy of p and q
    for i in range(len(p)):
        print(p[i] * np.log2(q[i]))
    return -np.sum(p * np.log2(q))

# create a binary distribution X, Y, and Z
X = np.array([1, 0])        
Y = np.array([0.8, 0.2])
Z = np.array([0.4, 0.6])

# calculate the cross entropies
H_XY = cross_entropy(X, Y)
H_XZ = cross_entropy(X, Z)
H_YZ = cross_entropy(Y, Z)

# print the results
print('H(X, Y) = %.3f bits' % H_XY)
print('H(X, Z) = %.3f bits' % H_XZ)
print('H(Y, Z) = %.3f bits' % H_YZ)
