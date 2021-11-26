#15. Omogućite unos niza znakova te ispišite sljedeće:
#	a) svaka neparna riječ (osim prve) iz niza mora biti ispisana malim znakovima po redu kako 
#    su bili unešeni
#	b) svaka parna riječ (osim posljednje parne) iz niza mora biti ispisana velikim znakovima, 
#    obrnutim redom od onog kako je bila unešena

n=input("unesi niz znakova")
lista=n.split()
a= str(lista[2::2])
if len(lista)%2==0:
    b=str(lista[-3::-2])
else:
    b= str(lista[-4::-2])


print(a.lower())
print(b.upper())

