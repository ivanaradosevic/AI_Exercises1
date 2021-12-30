# Proširite model iz prethodnog zadatka polinomskim članovima različitih stupnjeva.
# Zabilježite rezultate, te komentirajte ponašanje modela. Koju pojavu uočavate

from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures


ch_x, ch_y= datasets.fetch_california_housing(return_X_y=True)
nrows, ncols= 2, 4
fig= plt.figure()
for i in range(1,9):
    ax=fig.add_subplot(nrows,ncols, i)
    ax.scatter(ch_x[:,i-1],ch_y)
plt.show()

ch_x= ch_x[:,[0,7]]
poly= PolynomialFeatures(degree=2)
ch_x=poly.fit_transform(ch_x)


ch_x_train, ch_x_test, ch_y_train, ch_y_test= train_test_split(ch_x, ch_y, test_size=0.3)
linear_model=linear_model.LinearRegression()
linear_model.fit(ch_x_train,ch_y_train)
chy_pred= linear_model.predict(ch_x_test)

mse= mean_squared_error(ch_y_test, chy_pred)
r2=r2_score(ch_y_test, chy_pred)

plt.scatter(ch_x_test[:, 1], ch_y_test)
plt.scatter(ch_x_test[:,1], chy_pred, color= "red")
plt.show()

print(mse)
print(r2)
print(linear_model.coef_)

print("done")