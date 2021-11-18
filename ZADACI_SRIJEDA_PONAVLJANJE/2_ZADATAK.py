#2. Napravi obrtaljku od unesenog stringa te na svakom drugom mjestu pridruzi nasumičan broj.
import random
a= "Ivana"
b=a[::-1]
c=" "
for i in b:
    n=random.randint(1 , 9)
    c+=i+str(n)
print(c)

#pomogao mi je kolega, inače bi mi trebalo jakooo dugo da shvatim sama

