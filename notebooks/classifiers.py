＃ Data preprocessing

# Apply models

model_name = ["kNN", "Linear SVM", "Nonlinear SVM", "Decision Tree", "Naives Bayes", "ANN"]
models = [KNeighborsClassifier(n_neighbors = 3),
#SVM: linear & nonlinear
          SVC(kernel="linear", C=0.025),
          Pipeline((
              ("poly_features", PolynomialFeatures(degree=3)),
              ("scaler", StandardScaler()),
              ("svm_clf",LinearSVC(C=10, loss="hinge")))),
          DecisionTreeClassifier(max_depth=2),
          GaussianNB(),
          MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)]
