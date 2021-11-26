#8 Unesi neki nasumični broj kojeg ćeš uzeti kao vrijednost duljine liste u koju se trebaju spremiti 
# vrijednosti od 0 do 1001. 
#Ispiši sljedeće vrijednosti na ekran:
		#a) medijan
		#b) mod
		#c) aritmetičku vrijednost
		#d) sve brojeve koji se u definiranoj listi nalaze ispred vrijednosti 
        # koju smo izračunali kao medijan navedene liste
		#e) sve brojeve koji su manji od vrijednosti koju smo izračunali kao medijan navedene liste 

	#*Bonus: Napravite novu listu koja sadrži samo vrijednosti koje su za 10% veće 
    # ili manje od aritmetičke sredine

import random
import statistics
n=int(input("unesi neki nasumičan broj :"))
lista=[]
for i in range(0,n):
    n = random.randint(0,1001)
    lista.append(n)
min=statistics.mean(lista)
print(lista)                         #c) aritmeticka
print(min)

med= statistics.median(lista)
print(lista)                         #a) medijan
print(med)

mod= statistics.mode(lista) 
print(lista)                           #b) mod
print(mod)

lista1=[]
lista2=[]

for b in lista:
    if b>med:
        lista1.append(b)
    elif b<med:
        lista2.append(b)
print("brojevi veći od medijana su:", lista1, "brojevi manji od medijana su: ", lista2)

#*Bonus: Napravite novu listu koja sadrži samo vrijednosti koje su za 10% veće 
# ili manje od aritmetičke sredine

new_li=[]
dp= min*10/100
for s in lista:
    if s>min-dp and s<min+dp :              
        new_li.append(s)
print(new_li)









