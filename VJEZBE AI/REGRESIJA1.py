import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
xtrain =np.array([[0], [1], [2]])
ytrain = np.array([0,1,2])

plt.scatter(xtrain, ytrain)

plt.show()

linear_model= lm.LinearRegression()
linear_model.fit(xtrain, ytrain)

"""print(linear_model.coef_)  #coef je nagib pravca koji je 1 zato sto je x=y
print(linear_model.intercept_)  #2.220446049250313e-16 je 0, 10* na -16"""

#test

xtest=np.array([[0.5], [3]])
ypred=linear_model.predict(xtest) #uzimamo trening model i predviđamo
print(ypred)  #[0.5 3.] jer je x=y i tetni su isti
