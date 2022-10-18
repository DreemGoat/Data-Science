import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import  SVC
import numpy as np
from sklearn.metrics import accuracy_score

#dataset loading

bc = datasets.load_iris()
df = pd.DataFrame(data = bc.data)
df["label"] = bc.target
df.info()

#graph

plt.scatter(df[0][df["label"] == 0], df[1][df["label"] == 0],
            color='red', marker='o', label='Iris-Setosa')
plt.scatter(df[0][df["label"] == 1], df[1][df["label"] == 1],
            color='green', marker='*', label='Iris-Versicolour')
plt.scatter(df[0][df["label"] == 2], df[1][df["label"] == 2],
            color='purple', marker='x', label='Iris-Virginica')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend(loc='upper left')
plt.show()

X = df.iloc[:,0:2]
y = df['label']

svm = SVC(kernel ='rbf', random_state=1, gamma='auto', C=9)

#training the model
svm.fit(X,y)

def plot_contours(ax, clf, xx, yy, **params):
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    return xx, yy

fig, ax = plt.subplots()

title = ('SVC graph')

X0, X1 = X.iloc[:,0], X.iloc[:,1]
xx, yy = make_meshgrid(X0, X1)

plot_contours(ax, svm, xx, yy, cmap =plt.cm.YlGn, alpha=0.4)
ax.scatter(X0, X1, c=y, cmap=plt.cm.coolwarm, s=50,alpha=0.7)
ax.set_xlabel('Sepal length')
ax.set_ylabel('Sepal width')
ax.set_xticks(())
ax.set_yticks(())
ax.set_title(title)
plt.show()

y_pred=svm.predict(X)

# Show the performance of your model
print(accuracy_score(y, y_pred))