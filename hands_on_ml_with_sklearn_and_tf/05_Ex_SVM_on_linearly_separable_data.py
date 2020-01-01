import numpy as np
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

X,y = load_breast_cancer(return_X_y=True)
ratio = 0.8
m = X.shape[0]
train_size = int(ratio * m)
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
X_train = X_scaled[:train_size]
y_train = y[:train_size]
X_test = X_scaled[train_size:]
y_test = y[train_size:]

linsvc = LinearSVC(loss="hinge", C=5)
svc = SVC(C=5, kernel="linear", )
sgd = SGDClassifier()

for clf in [linsvc, svc, sgd]:
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = np.sum(y_pred == y_test) / len(y_test)
    print("Acc: {}",format(acc))
    # y_pred_0 = clf.predict(X_test[0].reshape(1,-1))
    # print("y: {}\t y_pred: {}".format(y_test[0], y_pred_0))


