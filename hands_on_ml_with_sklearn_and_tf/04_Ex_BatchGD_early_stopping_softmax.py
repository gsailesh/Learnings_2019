"""
Implement Batch Gradient Descent with early stopping for Softmax Regression
(without using Scikit-Learn).

- Split data into train, test
- convery ys to one hot vectors
- define a softmax function
- use early stopping and find theta
- calculate the accuracy from test set

"""
from sklearn.datasets import load_iris
import numpy as np

np.random.seed(102)

num_iter = 5001
tol = 1e-5
lr = 0.01
ratio = 0.8

X, y = load_iris(return_X_y=True)

m = len(X) 
train_size = int(ratio * m)
# random_indices = np.random.permutation(m)

def to_one_hot(y):
    n = y.max() + 1
    m = len(y)
    
    y_one_hot = np.zeros((m,n))
    y_one_hot[np.arange(m), y] = 1

    return y_one_hot

def softmax(logits):
    exps = np.exp(logits)
    exps_sum = np.sum(exps, axis=1, keepdims=True)
    
    return exps / exps_sum

def update_learning_rate(lr):
    return lr/(1 + lr)

X_b = np.c_[np.ones([X.shape[0],1]), X]

X_train = X_b[:train_size]
y_train = y[:train_size]
X_test = X_b[train_size:]
y_test = y[train_size:]

y_train_onehot = to_one_hot(y_train)
y_test_onehot = to_one_hot(y_test)

theta = np.random.randn(X_b.shape[1], len(np.unique(y_train)))

for i in range(num_iter):
    
    logits = X_train.dot(theta)
    y_proba = softmax(logits)

    cross_entropy_loss = np.mean(np.sum(y_train_onehot * np.log(y_proba), axis=1))
    error = y_proba - y_train_onehot
    
    if(i % 500 == 0):
        print("Iteration #: {}\t Loss: {}".format(i, cross_entropy_loss))

    gradients = (1/m) * X_train.T.dot(error)
    theta = theta - lr * gradients
    lr = update_learning_rate(lr)


test_logits = X_test.dot(theta)
y_proba_test = softmax(test_logits)

y_pred = np.argmax(y_proba_test, axis=1)

acc = np.mean(y_pred == y_test)
print("Accuracy: ".format(acc))