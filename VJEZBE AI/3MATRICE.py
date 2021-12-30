#3. napravite 3D matricu popunjenu random vrijednostima, ispisite ju te dohvatite neku koordinatu koju 
# korisnik unese.
#  ako  je vrijednost koordinate 0, ispisati "CRNA", ako je 10, ispisati "BIJELA".

import random
from random import randint

arr = []
for x in range(5):
    arr.append([])
    for y in range(5):
        arr[x].append([])
        for z in range(5):
            arr[x][y].append(random.randint(0, 10))
print(arr)

print('koju koordinatu zelite ispisati(matrica je dimezija 5x5x5?')
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

if arr[x-1][y-1][z-1] == 0:
    print('crna')
elif arr[x-1][y-1][z-1] == 10:
    print('bijela')