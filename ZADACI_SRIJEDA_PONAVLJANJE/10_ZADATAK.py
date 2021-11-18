#10. S tipkovnice učitajte proizvoljni niz znakova. Kreirajte novi niz 
#znakova koji će sadržavati naizmjence velika i mala slova iz ulaznog 
#niza, redom kako se pojavljuju u ulaznom nizu: prvo veliko slovo u 
#ulaznom nizu, prvo sljedeće malo slovo u nastavku ulaznog niza, 
#prvo sljedeće veliko slovo u nastavku ulaznog niza itd. Novokreirani 
#niz ispišite na zaslon. U nastavku se nalazi primjer:

#Ulazni niz: ifeFemFEkej83FkW
#Izlazni niz: FeFkFkW

n= input("upiši niz:")
novi= " "
veliko= True
for i in n:
    if i.isupper()==True and veliko==True:
        novi+=i
        veliko=False
    elif i.islower()==True and veliko==False:
        novi+=i
        veliko=True
print(novi)


