# 6. napravite program koji izracunava razliku dva unesena niza DNK (jednakih duljina).
#  npr. ako su uneseni: 
# "GAGCCTACTAACGGGAT" i 
# "CATCGTAATGACGGCCT"
#  x x x  x x    xx
# program treba ispisati da je razlika 7. mozete li ispisati i parove koji nisu u redu?

a="GAGCCTACTAACGGGAT"
b= "CATCGTAATGACGGCCT"
parovi_razlike=[]
for i in range(len(b)):
    if a[i] !=b[i]:
        parovi_razlike.append([a[i], b[i]])
print(parovi_razlike)
