# 1. napravite klasu za pogadjanje brojeva. program treba odrediti random interval brojeva 
# [-random, random] te iz njega uzeti broj koji se nalazi u sredini (postavi granice randoma 
# za granice intervala na 1000). traziti unos od korisnika da unese broj koji je program odredio. 
# Ako se broj nalazi u intervalu, program treba ispisati: "toplo", ako je njegov iduci unos blizi
#  broju koji se od njega trazi, treba ispisati: "toplije", a ako unese broj koji se nalazi izvan 
#  intervala, treba ispisati poruku: "hladno". ispisite i broj koraka koje je korisnik trebao
#  napraviti da bi dosao do rjesenja.

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
                
        
p = Pogodi_broj()
p.pogod()


        