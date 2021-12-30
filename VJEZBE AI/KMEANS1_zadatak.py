# Učitajte Mall_Customers.csv podatke. Koristeći Spending_score veličinu, te jednu veličinu po
# izboru odredite centre klastera koristeći Kmeans algoritam.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd


data=pd.read_csv("Mall_Customers.csv")
X=data.iloc[:,[3,4]].values
kmeans=KMeans(3)
kmeans.fit(X) #funkcija za treniranje

print(kmeans.cluster_centers_)








