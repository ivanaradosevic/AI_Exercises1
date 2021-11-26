#14. Kreirajte varijablu te u nju spremite nasumični niz znakova. 
#Na ekran s jednom print naredbom ispišite sljedeće: 
#a) “prva riječ u nizu ima sva velika slova bez obzira na uneseni niz: <RIJEČ>” 
#b) “druga riječ u nizu ima <XY> znakova”
#c) “ne postoje bjeline iza unesenog niza znakova: <niz znakova>” 
#d) “ne postoje bjeline prije unesenog niza znakova: <niz znakova>” 
#e) “svi znakovi su ispisani malim slovom: <niz znakova>”, 
#f) “samo prvo slovo cijelog niza je ispisano velikim slovom te je iza unesenog niza dodan 
# niz “ asdfčlkasdfčlk” odmah nakon zadnjeg alfanumeričkog znaka: <niz znakova + ostatak>”

n= input("upiši neki nasumični niz znakova")
l=n.split()
print("prva riječ u nizu ima sva velika slova bez obzira na uneseni niz",l[0].upper())
print(f"druga riječ u nizu ima, {len(l[1])}, znaka")
print("ne postoje bjeline iza unesenog niza znakova", n.rstrip())
print("ne postoje bjeline prije unesenog niza znakova", n.lstrip())
print("svi znakovi su ispisani malim slovom", n.lower())
print("samo prvo slovo cijelog niza je ispisano velikim slovom te je iza unesenog niza dodan niz'asdfčlkasdfčlk'odmah nakon zadnjeg alfanumeričkog znaka ", 
n.capitalize().rstrip() + "asdfčlkasdfčlk")
