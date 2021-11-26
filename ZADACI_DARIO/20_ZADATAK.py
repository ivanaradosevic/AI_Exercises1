#20. Omogućite korisniku unos dviju vrijednosti n puta. 
#Sortirajte sve unose koristeći druge vrijednosti iz svakog unosa.

n=int (input("koliko unosa želite: "))

lista=[]
for i in range(0,n):
    b=input("unesi dvije vrijednosti: ").split(",")
    lista.append(b)

lista.sort(key=lambda x: x[1])
print(lista)



