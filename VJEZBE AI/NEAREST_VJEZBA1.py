# Izgradite klasifikator koristeći logističku regresiju čiji je izlaz binarna vrijednost koja
# označava postoji li šansa za srčani udar na temelju informacija / nalaza pacijenta zapisanih
# u heart.csv
# datoteci.
# Opis ulaznih veličina:
# 1) age
# 2) sex
# 3) chest pain type (4 values)
# 4) resting blood pressure
# 5) serum cholestoral in mg/dl
# 6)fasting blood sugar > 120 mg/dl
# 7) resting electrocardiographic results (values 0,1,2)
# 8) maximum heart rate achieved
# 9) exercise induced angina
# 10) oldpeak = ST depression induced by exercise relative to rest
# 11)the slope of the peak exercise ST segment
# 12) number of major vessels (0-3) colored by flourosopy
# 13) thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
# 14) target: 0= less chance of heart attack 1= more chance of heart attack
# Koristeći testne podatke izradite / odredite:
# 1. Matricu zabune
# 2. Preciznost
# 3. Odziv
# 4. F1 mjer


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("heart.csv")
X=data.iloc[:,:-1].values
y=data.iloc[:,-1].values


X= StandardScaler().fit_transform(X)
x_train, x_test, y_train, y_test=train_test_split(X, y, test_size= 0.2)

classiffier= KNeighborsClassifier(n_neighbors=3)
classiffier.fit(x_train, y_train)
y_pred=classiffier.predict(x_test)

conf_matrix=confusion_matrix(y_test, y_pred)
report=classification_report(y_test, y_pred)
print(conf_matrix)
print(report)
