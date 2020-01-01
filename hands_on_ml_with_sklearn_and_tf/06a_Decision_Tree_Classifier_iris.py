from sklearn.datasets import load_iris
from sklearn.tree import export_graphviz, DecisionTreeClassifier

# X,y = load_iris(return_X_y=True)
iris_data = load_iris()
X = iris_data["data"]
y = iris_data["target"]

model = DecisionTreeClassifier(max_depth=3)
model.fit(X,y)

export_graphviz(model, out_file="/home/saileshg/sailspace/dev2019/hands_on_ml_with_sklearn/Reboot/tree_out.dot", 
feature_names=iris_data["feature_names"], class_names=iris_data["target_names"], 
filled=True)