"""
Showcases how confusion matrix works.

- Rows represent actual class, Columns represent predicted class
- Normalizing the conmat values with row sums and then ignoring the diagonal values,
  would emphasize the misclassifications. This is plotted here.

"""

from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]

conmat = confusion_matrix(y_true, y_pred, ["ant", "bird", "cat"])
print(conmat)

row_sums = conmat.sum(axis=1, keepdims=True)
print(row_sums)
norm_conmat = conmat/row_sums

print(norm_conmat)

np.fill_diagonal(norm_conmat, 0)
print(norm_conmat)

plt.matshow(norm_conmat, cmap=plt.cmap.gray)
plt.show()