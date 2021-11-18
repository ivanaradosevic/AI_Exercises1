#7. Ispiši vrijednost broja Pi na 4 decimalna mjesta, 
# kvadriraj taj broj te ga podijeli s racionalnim brojem odabranim od strane korisnika
# (input funkcija) i ispiši rezultat.

import math

p= str(math.pi)
i=p[:6]
pi= float(i)
print(pi)

n= float(input("upiši neki broj: "))           #kada se traži racionalni broj, onda je to float!
rezultat= pi**2/n
print("rezultat je", rezultat)

