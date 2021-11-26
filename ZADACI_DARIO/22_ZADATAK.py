#22. Napravite funkciju koja prima brojeve i vraća redom:
#	a) umnožak tih brojeva
#	b) zbroj tih brojeva 
#	c) poredak po veličini (descending)
#	d) tuple prostih brojeva koji su unešeni
#	e) tuple parnih brojeva koji su unešeni
#	*uzmite rezultate te funkcije te ih zapišite u file def_rez.txt

n= (input("upiši neke brojeve s zarezom: ").split(","))
lista=[]
for i in n:
    b=int(i)
    lista.append(b)
def funky(lista):
    umnozak=1
    for i in lista:
        umnozak*=i
    print("umnozak unesenih brojeve je", umnozak)

    zbroj= 0
    for i in lista:
        zbroj+=i
    print("zbroj je ", zbroj)
    lista.sort()
    print("Descending order", lista[::-1])

    pros=[]
    for i in lista:
        if i >1:
            for j in range(2,int(i,2)+1):
                if(i%j)==0:
                    break
            else:
                pros.append(i)
    pros=tuple(pros)
    print("prosti brojevi su: ", pros)

    return umnozak, zbroj, lista[::-1],pros, 

        









