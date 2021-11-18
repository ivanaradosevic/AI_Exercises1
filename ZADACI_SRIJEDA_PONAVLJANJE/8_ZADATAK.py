#8. Napišite program koji s tipkovnice učitava proizvoljni cijeli 
#troznamenkasti broj. Ako učitani broj nije troznamenkasti, ispišite 
#poruku o greški i prekinite daljnje izvođenje programa. U slučaju da 
#je učitani broj ispravan, ispišite prvi sljedeći troznamenkasti 
#palindrom. Na primjer, ako je učitani broj 120, prvi sljedeći palindrom 
#je 121.
#od početka prema kraju ili obrnuto glase jednako


while True:
    n=input("upiši trozn. broj: ")
    if len(n)!=3:
        print("pogrešno")
        break
    elif len(n)==3:
        if n[0]==n[-1]:
            print("uneseni broj je palindrom")
        elif int(n[0])>int(n[-1]):
            print("prvi slj palindrom je:", n[0:2]+n[0])
        elif int(n[0])<int(n[-1]):
            print("prvi slj palindrom je:", n[0]+str(int(n[1])+1)+n[0])

            #ne bih riješila zadatak bez pomoći