"""
Train and fine-tune a Decision Tree for the moons dataset.

a. Generate a moons dataset using make_moons(n_samples=10000, noise=0.4)
b. Split it into a training set and a test set using train_test_split()
c. Use grid search with cross-validation (with the help of the GridSearchCV
class) to find good hyperparameter values for a DecisionTreeClassifier

Hint: try various values for max_leaf_nodes .

d. Train it on the full training set using these hyperparameters, and measure
your model’s performance on the test set. You should get roughly 85% to 87%
accuracy

"""
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier

X,y = make_moons(n_samples=10000, noise=0.41)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=43)

model = DecisionTreeClassifier()

param_grid = {"criterion":['gini', 'entropy'], "max_depth":[2,3,4,5], "max_leaf_nodes":[2,3,4,6,8]}
grid = GridSearchCV(model, param_grid, cv=5, verbose=1)

grid.fit(X_train, y_train)

print("Best params: {} Best score: {}".format(grid.best_params_, grid.best_score_))
grid.fit(X, y)

print("Best params on full training set: {} Best score on full training set: {}".format(grid.best_params_, grid.best_score_))

final_model = grid.best_estimator_

