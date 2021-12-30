# a. Učitajte California housing skup podataka iz Scikit-learn dataset modula.
# b. Eksplorativnom analizom podataka istražite odnose među varijablama.
# c. Odaberite jednu ulaznu veličinu i podijelite podatke na trening i testni skup u
# odnosu 70%-30%.
# d. Izgradite linearni model.
# e. Vrjednovanjem modela odredite srednju kvadratnu pogrešku i koeficijent
# determinacije

from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score


ch_x, ch_y= datasets.fetch_california_housing(return_X_y=True)
nrows, ncols= 2, 4
fig= plt.figure()
for i in range(1,9):
    ax=fig.add_subplot(nrows,ncols, i)
    ax.scatter(ch_x[:,i-1],ch_y)
plt.show()

ch_x= ch_x[:,0]
ch_x=ch_x[:,np.newaxis]

ch_x_train, ch_x_test, ch_y_train, ch_y_test= train_test_split(ch_x, ch_y, test_size=0.3)
linear_model=linear_model.LinearRegression()
linear_model.fit(ch_x_train,ch_y_train)
chy_pred= linear_model.predict(ch_x_test)

mse= mean_squared_error(ch_y_test, chy_pred)
r2=r2_score(ch_y_test, chy_pred)

print(mse)
print(r2)
print(linear_model.coef_)

print("done")



