#4. Napišite program koji će u varijable a i b spremiti dva dvoznamenkasta broja. 
# U varijablu a pohranite zadnju znamenku broja koji se nalazi u varijabli b, 
# a u varijablu b pohranite zadnju znamenku broja koja se nalazi u varijabli a. 
#Ispišite sadržaj varijabli a i b.

a=12
b=25
znm = a
a = b
b = znm
a = a%10
b %= 10
print(a, b)