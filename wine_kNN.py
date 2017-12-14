from sklearn import neighbors
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn import metrics

wine = load_wine()
X, y = wine.data, wine.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
predicted = knn.predict(X_test)

print(metrics.classification_report(y_test, predicted))
print("Confusion matrix: \n"+ str(metrics.confusion_matrix(y_test, predicted)))
