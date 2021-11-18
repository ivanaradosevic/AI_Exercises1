#9.Napišite program koji učitava cijele brojeve sve dok je unesena 
#vrijednost veća od 0. Pronađite koji od učitanih brojeva ima najmanju 
#sumu znamenki te ispišite taj broj i sumu.

n= int(input("unesi cijeli broj"))

br=[]
zb=[]

while n>0:
    br.append(n)
    n=int(input("unesi cijeli broj"))
for i in br:
    zbroj=0
    for j in str(i):
        zbroj+=int(j)
    zb.append(zbroj)

su=min(zb)
ind=zb.index(su)
print("broj koji ima najmanju znamenku je:" ,br[ind],"suma je:" ,su)
