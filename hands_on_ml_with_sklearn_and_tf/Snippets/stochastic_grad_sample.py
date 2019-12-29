import numpy as np

m = 100
epochs = 50

X = 2 * np.random.randn(m,1)
X_b = np.c_[np.ones((m,1)), X]
y = 4 + 3 * X + np.random.randn(m,1)

theta = np.random.randn(2,1)
lr = 0.01

for _ in range(epochs):
    for i in range(m):
        xi = X_b[i:i+1]
        yi = y[i:i+1]

        gradients =  2 * xi.T.dot(xi.dot(theta) - yi)
        theta = theta - lr * gradients

print(theta)