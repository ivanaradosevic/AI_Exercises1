#4. napravite jednostavniju verziju igre potapanja brodova. neka se ploca za igru sastoji od matrice,
#  a program neka odredi neke random koordinate na kojima se nalazi protivnicki brod. zadatak igraca je 
# potopiti sve brodove. 
# neka se ispise prikladna poruka ako je brod pogodjen, 
# promasen ili ako vise ne postoji protivnickih brodova na ploci.

import random
from random import randint

matrix = [[0 for j in range(10)] for i in range(10)]
broj_brodova = random.randint(5, 10)
for i in range(broj_brodova):
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    matrix[a-1][b-1] = 1
for lst in matrix:
    print(lst)
count = 0
for i in range(10):
    for j in range(10):
        if matrix[i][j] == 1:
            count += 1

while count>0:
    print('koju koordinatu zelite potopiti?')
    x = int(input('x: '))
    y = int(input('y: '))

    if matrix[x-1][y-1] == 'X':
        print('Sucess')
        matrix[x - 1][y - 1] = 0
        count -= 1

    elif matrix[x-1][y-1] != 1:
        print('Fail!')

if 'X' not in matrix:
    print('NO more boats')

