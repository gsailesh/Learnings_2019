from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

X, y = load_iris(return_X_y=True)

softmax_regressor = LogisticRegression(solver='lbfgs', multi_class='multinomial', verbose=1, C=10)
softmax_regressor.fit(X, y)

print("Class: {0}, Probabilities: {1}".format(softmax_regressor.predict([[5, 2, 1, 0.3]]), softmax_regressor.predict_proba([[5, 2, 1, 0.3]])))
