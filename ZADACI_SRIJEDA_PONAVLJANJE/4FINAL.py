# 4. napravite program koji ucitava podatke iz prethodno napravljenih datoteka te dodatno 
# ispisuje ukupan broj redaka, prosjecan broj koraka (za prvi zadatak), odnosno prosjecan postotak 
# pogodaka (za drugi zadatak)

import re

f=open("pogadanje.txt", "r", encoding="utf-8")
data= f.read()

print(data)

a=re.findall(r"\w\Z",data)
print(a)

f=open("lutrija.txt","r", encoding="utf-8")
data2=f.read()
f.close()

b=re.findall(r"\w+.\w+\Z", data2)
print(b)