#5. Omogućite unos 8 racionalnih brojeva te ispišite rezultat po sljedećoj formuli: 
# a+ b / c * d**e // f - g % h 
#- komentarima ispišite što se sve događa kroz nekoliko slučajeva upisanih različitih brojeva
liste=[]
for i in range(8):
    a=float(input("unesi broj"))
    liste.append(a)
print(liste)

a= (liste[0])
b= (liste[1])
c= (liste[2])
d= (liste[3])
e= (liste[4])
f= (liste[5])
g= (liste[6])
h= (liste[7])
print(a + b/c*d**e//f-g%h)
#prvo sam kreirala listu kako bih podatke spremila, zatim sam preko for petlje i inputa dohvaćala 
#racionalne brojeve, spremili su se u listu iz koje je dobiven izračun formule.