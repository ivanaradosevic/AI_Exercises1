#1. napravite 2D matricu dimenzija 10, postavite vrijednosti pomocu random(0, 10) i ispisite ju + 2 zadatak.
#a)dijagonale matrice
#b) b) stupce matrice odvojene zarezom
# c) koordinate: [3, 8], [10, 10], [5, 5] - nadogradite tako da korisnik moze unijeti koordinate koje 
# zeli ispisati.

import random

matrica=[]

for i in range (10):
    lista=[]
    matrica.append(lista)
    for j in range(10):
        broj=random.randint(0,10)
        lista.append(broj)
for i in matrica:
    print(i)  

b=0
dijagonale=[]
for i in matrica:
    dijagonale.append(i[b])
    b+=1
print("dijagonale su: ", dijagonale)

stupci=[]
brojacic=0
for z in range (10):
    stupac=[]
    for i in matrica:
        stupac.append(i[brojacic])
    brojacic+=1
    stupci.append(stupac)
print("stupci su:", stupci)

a=int(input("unesite prvu koordinatu odvojenu zarezom: "))
b=int(input("unesite drugu koordinatu odvojenu zarezom: "))

print(matrica[a-1][b-1])

