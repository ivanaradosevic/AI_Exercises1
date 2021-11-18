"""14. Odaberite proizvoljno koordinatu T=(x,y), vrijednosti varijabli x
(stupac) i y (redak) neka budu manje od 10. Program neka ispiše 
polje 10x10 čiji su svi elementi vrijednosti "-" osim koordinate T čija 
je vrijednost "X". 

Primjer: T=(1,1)
- - - - - - - - - -
- X - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
"""
x= int(input("unesi broj 0-9"))
y=int(input("unesi još jedan broj od 0-9"))

for i in range(y):
    print(" - "*10)
print(" - "*x, "X", " - "*(9-x))
for j in range(9-y):
    print(" - "*10)

#riješen uz pomoć