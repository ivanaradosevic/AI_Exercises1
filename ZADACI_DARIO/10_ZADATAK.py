#11. U varijablu upišite neki proizvoljni niz znakova. Nad varijablom pozovite odgovarajuću 
# funkciju koja će vratiti duljinu upisanoga niza znakova te rezultat spremite u novu varijablu. 
# Ispišite sve znakove do polovice niza. 
#Primjer: ako imamo niz od 15 znakova (abcdefghijklmno), 
# potrebno je ispisati 1., 2., 3., 4., 5., 6., 7. i 8. znak (abcdefgh)

a= "abcdefghijklmno"
duljina=len(a)
print(a[0:int(duljina/2)])

