#19. Omogućite unos dviju vrijednosti u dva navrata korisniku.
#Svaki par vrijednosti zapišite u jedan tuple.
#Zamijenite vrijednosti ovih dvaju tupleova te ispišite rezultat.

a= tuple(input("upiši prvu vrijednost: ").split(","))
b= tuple(input("upiši drugu vrijednost: ").split(","))
print ("a=",a, "b=",b)
(a,b)=(b,a)
print("a=",a, "b=",b)




