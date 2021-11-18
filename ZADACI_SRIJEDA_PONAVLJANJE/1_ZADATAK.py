#1. Napiši program koji učitava listu i briše sve duplikate iz te liste te ispisuje novu listu s 
#obrisanim duplikatima

a=[3, 5, 7, 8, 2, 4, 8, 3, 1]
pr=[]
for i in a:
    if i not in pr:
        pr.append(i)
print(pr)

#DRUGI NAČIN

lista=input("unesi podatke: ").split(",")
nova_li=list(set(lista))
print(nova_li)
        


