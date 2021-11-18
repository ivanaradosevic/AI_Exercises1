#13. Spremite sljedeći niz znakova u varijablu: "Testiramo što sve možemo napraviti sa stringovima". 
# Iz niza znakova u prethodnom zadatku dohvatite i ispišite: 
#a) cijeli niz
#b) riječ "string", 
#c) koji je to tip podatka,
#d) koje je početno slovo te riječi koristeći indekse
#e) koje je posljednje slovo te riječi koristeći metode za stringove
#f) koliko znakova ta riječ ima 

a= "  Testiramo što sve možemo napraviti sa stringovima  "
print(a)
print(a[::-1]) #nije u zadatku

rij= a.split()
r=rij[-1]
print(rij[-1])
print(r.removesuffix("ovima"))

#string je niz podataka, tj, znakovni niz, kako bi se u varijable mogao spremati tekst, 
# označava se dvostrukim ili jednostrukim navodnim znacima

print(r[0]) #pocetno slovo je T

print(type(r))  #tip podatka

endswith???










