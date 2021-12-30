# 2. u klasi iz prethodnog zadatka napravi "pseudo lutriju" 6/39, odnosno program koji bi 
# od 0-39 brojeva uzeo nasumicnih 6 (bez ponavljanja) i trazio od korisnika unos brojeva. 
# kada korisnik unese tih 6 brojeva, treba ispisati koliko brojeva je korisnik pogodio i 
# njegov postotak tocnosti (npr. ako je pogodio 3 broja, treba ispisati 50%). nadogradite 
# program tako da prima varijable umjesto brojeva 39 i 6 i neka se korisnika pita za unos istih 
# (npr. 52 i 3, odnosno 3/52).

import random
class Pogodi_broj:
    def __init__(self):
        self.granica = random.randint(0,1000)
        self.broj_koji_pogadjamo = self.granica // 2
        
    def pogod(self):
        korisnikov_broj=0
        brojac=0
        while True:
            prethodni_broj=korisnikov_broj    
            korisnikov_broj=int(input("upiši broj: "))
            brojac+=1
        
            if korisnikov_broj == self.broj_koji_pogadjamo:
                print("pogodili ste")
                print(f"trebalo vam je{brojac} pokušaja")
                break
            elif korisnikov_broj > 0 and korisnikov_broj < self.granica:
                print("toplo")
                while korisnikov_broj > 0 and korisnikov_broj < self.granica:
                    prethodni_broj=korisnikov_broj    
                    korisnikov_broj=int(input("upiši broj: "))
                    brojac+=1
                    if korisnikov_broj < self.broj_koji_pogadjamo:
                        razlikak=self.broj_koji_pogadjamo-korisnikov_broj
                    elif korisnikov_broj > self.broj_koji_pogadjamo:
                        razlikak=korisnikov_broj-self.broj_koji_pogadjamo
                    if prethodni_broj < self.broj_koji_pogadjamo:
                        razlikap= self.broj_koji_pogadjamo-prethodni_broj
                    elif prethodni_broj > self.broj_koji_pogadjamo:
                        razlikap=prethodni_broj-self.broj_koji_pogadjamo
                    if razlikak > razlikap:
                        print("hladnije")
                    elif razlikak < razlikap:
                        print("toplije")
                    if korisnikov_broj == self.broj_koji_pogadjamo:
                        print("pogodili ste")
                        print(f"trebalo vam je {brojac} pokušaja")
                        break
        
            
            elif korisnikov_broj > 0 and korisnikov_broj > self.granica:
                print("hladno")

    def lutrija(self):
        lista=[]
        kl=[]
        pogbr=0
        while len(lista)<=5:
            b=random.randint(0,39)
            if b not in lista:
                lista.append(b)
        while len(kl)<=5:
            n=int(input("izaberi broj do 39: "))
            kl.append(n)
        for i in kl:
            if i in lista:
                pogbr+=1
        postotak=pogbr/6*100
        print("Nagradni br su", lista)
        print("brojevi koje ste izabrali: ", kl)
        print("pogodili ste:", pogbr, "brojeva", postotak, "posto")       
                


p = Pogodi_broj()
p.lutrija()

       


        