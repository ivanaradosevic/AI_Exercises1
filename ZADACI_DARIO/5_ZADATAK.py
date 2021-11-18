#6. Unesi jedan nasumični broj. 
#Ispiši aritmetičku sredinu onoliko brojeva(0-101) koliko je iznosio uneseni nasumični broj.
#Navedeni broj uzmi kao vrijednost opsega kruga te ispiši vrijednost polumjera navedenog kruga.

import math
import statistics
import random
n=15
lista=[]
for i in range(0,n):
    n = random.randint(0,101)
    lista.append(n)
min=statistics.mean(lista)
print(lista)
print(min)

r=min/(2*math.pi)
print(r)