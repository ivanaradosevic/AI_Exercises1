# 3. zapisite intervale, brojeve, pogadjanja i postotke tocnosti u zasebne datoteke (imenujte ih po zelji). neka izgled unutar datoteke bude zapisan na sljedeci nacin: 
# 	a) za prvi zadatak --> [min, max] | uneseni_brojevi[broj1, broj2, broj3, ...] | broj_koraka
# 	b) za drugi zadatak --> 6/39 | uneseni_brojevi[broj1, broj1, broj3, ...] | postotak_pogodaka

import random
class Pogodi_broj:
    def __init__(self):
        self.granica = random.randint(0,1000)
        self.broj_koji_pogadjamo = self.granica // 2
        
    def pogod(self):
        uneseno=[]
        korisnikov_broj=0
        brojac=0
        pogib=False
        while True:
            if pogib==True:
                break
            prethodni_broj=korisnikov_broj    
            korisnikov_broj=int(input("upiši broj: "))
            uneseno.append(korisnikov_broj)
            brojac+=1
        
            if korisnikov_broj == self.broj_koji_pogadjamo:
                print("pogodili ste")
                print(f"trebalo vam je{brojac} pokušaja")
                f=open("pogadanje.txt","w")
                rez=str(f"[{min(uneseno)}, {max(uneseno)}] | {uneseno} | {brojac}\n")
                f.write(rez)
                f.close()
                break
            elif korisnikov_broj > 0 and korisnikov_broj < self.granica:
                print("toplo")
                while korisnikov_broj > 0 and korisnikov_broj < self.granica:
                    prethodni_broj=korisnikov_broj    
                    korisnikov_broj=int(input("upiši broj: "))
                    uneseno.append(korisnikov_broj)
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
                        f=open("pogadanje.txt","a",encoding="utf-8")
                        rez=str(f"[{min(uneseno)}, {max(uneseno)}] | {uneseno} | {brojac}\n")
                        f.write(rez)
                        f.close()
                        pogib=True
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
        f=open("lutrija.txt","a",encoding="utf-8")
        rez=str(f"6/39 | {kl} | {postotak}\n")
        f.write(rez)
        f.close()     
                


p = Pogodi_broj()
p.lutrija()
p.pogod()

