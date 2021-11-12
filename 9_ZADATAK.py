#10. Napišite algoritam koji uzima broj nasumične dužine te ispisuje:
#a) svaku drugu znamenku s tri decimalna mjesta (0,000) 
#b) zaokružen zbroj svih upravo ispisanih znamenki

a= input("upiši broj: ")
n1= (a[1::2]) #krece od prvog, pa do kraja, po dva koraka!
zb= 0
for i in n1:
    print(f"{i}.000")
    b=int(i)
    zb+=b
print(zb)


    
