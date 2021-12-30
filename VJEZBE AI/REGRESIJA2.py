from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

diabete_X, diabete_y=datasets.load_diabetes(return_X_y=True)
"""nrows, ncols=2,5
fig = plt.figure()
for i in range(1,11):
        fig.add_subplot(nrows, ncols, i)
        ax= fig.add_subplot(nrows, ncols,i)
        ax.scatter(diabete_X[:, i-1], diabete_y)
plt.show()"""

diabete_X=diabete_X[:,2]
diabete_X= diabete_X[:, np.newaxis]

poly= PolynomialFeatures(degree=3)
diabete_X=poly.fit_transform(diabete_X)

diabete_X_train, diabete_X_test, diabete_y_train, diabete_y_test=train_test_split(diabete_X, diabete_y, test_size=0.2)
linear_model=linear_model.LinearRegression()
linear_model.fit(diabete_X_train, diabete_y_train)
diabete_y_pred=linear_model.predict(diabete_X_test)
mse=mean_squared_error(diabete_y_test, diabete_y_pred)
print(mse)
r2=r2_score(diabete_y_test, diabete_y_pred)
print(r2)

plt.scatter(diabete_X_test[:, 1], diabete_y_test)
plt.scatter(diabete_X_test[:,1], diabete_y_pred, color= "red")
plt.show()

"""plt.scatter(diabete_X_test, diabete_y_test)
plt.plot(diabete_X_test, diabete_y_pred, color="blue", marker="o")
plt.show()"""





print("done")



