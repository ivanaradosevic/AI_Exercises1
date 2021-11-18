#7. Učitajte s tipkovnice 2 niza znakova, svaki od tih nizova znakova 
#spremite u zasebnu varijablu. Ispišite indekse na kojima se pojavljuju 
#ista slova neovisno o veličini ('a' i 'A' tretirati jednako).

a=input("upiši niz")
b=input("upiši niz")
c=a.lower()
d=b.lower()
for i in  c:
    if i in d:
        print("znak", i, "nalazi se na indexima:", c.find(i),"i", d.find(i))
