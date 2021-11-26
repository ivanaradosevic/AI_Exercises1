#16. Unesite dva proizvoljna niza znakova te ih spremite u dvije varijable. 
#Prvi niz znakova mora imati više unesenih riječi od drugog niza znakova.
#Od vrijednosti te dvije varijable napravite dvije liste te kreirajte konačni 
#rječnik gdje će vrijednosti iz druge liste biti ključevi, a vrijednosti iz prve 
#liste postati vrijednosti koje se pozivom ključa ispisuju.

values= list(["Ivana", "još malo" ,"ide", "doma Yoko"])
keys= list(["Yoko", "čeka", "Ivanu"])
dictionary = dict(zip(keys, values))
print(dictionary)

#ili

a=input("upiši niz znakova")
b=input("upiši nekoliko znakova, manje od prvog unosa")
c=a.split()
d=b.split()
dictionary = dict(zip(d, c))
print(dictionary)
