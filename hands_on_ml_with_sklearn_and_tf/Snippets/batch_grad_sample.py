import numpy as np

lr = 0.01
m = 100
n_iter = 1000

X = 2 * np.random.rand(m,1)
X_b = np.c_[np.ones((m,1)), X]
y = 4 + 3*X + np.random.randn(m,1)

theta = np.random.randn(2,1)

for _ in range(n_iter):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y) # gradient = (2/m) * X(theta.X - y)
    theta = theta - lr * gradients

print(theta)