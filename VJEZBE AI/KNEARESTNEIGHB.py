from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, classification_report
#from sklearn.preprocessing import StandardScaler

iris_x, iris_y=load_iris(return_X_y=True)

#iris_x= StandardScaler().fit_transform(iris_x)
x_train, x_test, y_train, y_test=train_test_split(iris_x, iris_y, test_size= 0.15)

classiffier= KNeighborsClassifier(n_neighbors=5)
classiffier.fit(x_train, y_train)
y_pred=classiffier.predict(x_test)

conf_matrix=confusion_matrix(y_test, y_pred)
report=classification_report(y_test, y_pred)
print(conf_matrix)
print(report)





#data= load_iris(as_frame=True)#sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) za vidjeti podatke
#print(data.data)
print("done")
