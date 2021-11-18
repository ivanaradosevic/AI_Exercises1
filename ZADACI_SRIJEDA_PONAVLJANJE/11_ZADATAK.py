#11. Napišite program koji s tipkovnice učitava cijeli broj n iz intervala [3, 
#20]. U slučaju da je unesena vrijednost neispravna, ispisati prikladnu 
#poruku na ekran te zatražiti ponovni unos cijelog broja. Nakon 
#učitane vrijednosti n, učitajte n parova cijelih brojeva. Nakon što je n
#parova brojeva učitano, ispišite parove brojeva koji imaju najveću 
#sumu.



while True:
    num=int(input("upiši cijeli broj od 3 do 20 :"))
    if num >= 3 and num <= 20:
        break
    else:
        print("broj nije valjan pokušajte ponovno")
parovi=[]
sume=[]
for i in range (num):
    a=int(input("unesi prvi broj"))
    b=int(input("unesi drugi broj"))
    zbroj= a+b
    par=str(a)+ " + " +str(b)
    parovi.append(par)
    sume.append(zbroj)

maks=max(sume)
index=sume.index(maks)
print(f"parovi brojeva s najvećom sumom su: ({parovi[index]}) sa sumom od :{maks}")  


    






