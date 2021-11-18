#6. S tipkovnice učitavajte cijele brojeve. Prvi upisani broj može biti bilo 
#koji cijeli broj. Učitavanje ponavljati dok god je upisani broj strogo 
#veći od prethodno upisanog broja. Ispisati sumu svih učitanih brojeva 
#osim broja zbog kojeg je prekinuto učitavanje.
a=[]
n= int(input("upiši brojeve: "))
a.append(n)
while True:
    n= int(input("upiši brojeve: "))  
    if n > max(a):
        a.append(n)
    else:
        break
print(sum(a))

    #znala sam s čime trebam krenuti na početku, ali bez kolege opet, ne bih ga uspjela riješiti
        
        
    

    
