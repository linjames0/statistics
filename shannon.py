# calculate the Shannon entropy of several distributions
import numpy as np
import matplotlib.pyplot as plt

def shannon_entropy(p):
    # calculate the Shannon entropy of a distribution

    return -np.sum(p * np.log2(p))

# create distributions X (normal), Y (uniform), and Z (deterministic)
X = np.random.normal(size=1000)
Y = np.random.uniform(size=1000)
Z = np.zeros(1000)
Z[0] = 1

# calculate the histograms
X_hist, _ = np.histogram(X, bins=10, range=(-3, 3))
X_hist = X_hist / float(np.sum(X_hist))
Y_hist, _ = np.histogram(Y, bins=10, range=(0, 1))
Y_hist = Y_hist / float(np.sum(Y_hist))
Z_hist = np.array([0.999, 0.001])

# calculate the entropies
H_X = shannon_entropy(X_hist)
H_Y = shannon_entropy(Y_hist)
H_Z = shannon_entropy(Z_hist)

# print the results
print('H(X) = %.3f bits' % H_X)
print('H(Y) = %.3f bits' % H_Y)
print('H(Z) = %.3f bits' % H_Z)

# plot the distributions
plt.figure()
plt.subplot(311)
plt.bar(range(10), X_hist, width=1)
plt.subplot(312)
plt.bar(range(10), Y_hist, width=1)
plt.subplot(313)
plt.bar(range(2), Z_hist, width=1)
plt.show()
