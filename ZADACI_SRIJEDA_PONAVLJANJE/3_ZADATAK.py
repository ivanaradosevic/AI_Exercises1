#3.Napiši program koji upisuje bodove n plesnih natjecanja. Ispiši zbroj svih bodova tako da odbaciš 
#najbolji i najlošiji rezultat.

a=int(input("upiši broj natjecanja: "))
bodovi=[]
for i in range(1, a+1):
    b= int(input("koliko bodova: "))
    bodovi.append(b)
print(sum(bodovi)-min(bodovi)-max(bodovi))


"""lista=[]
for i in range(5):
    a=int(input ('upisi broj'))
    lista.append(a)
print (sum(lista)-min(lista)-max(lista))
"""

#moram još vjezbati, tesko mi je bilo rijesiti zadatak...opet uz pomoc kolege sam ga rijesila


