#12. Napišite program koji s tipkovnice učitava proizvoljni niz znakova. 
#Nad učitanim nizom znakova napravite analizu je li taj niz palindrom 
#ili nije. Niz je palindrom ako se isto čita slijeva nadesno ili pak 
#zdesna nalijevo.

n=input("upiši neki niz: ")
m=n[::-1]

if m==n:
    print("palindrom je")
else: print("nije palindrom")



#DRUGI NAČIN S FUNKCIJOM

n= input("upiši neki niz: ")


def isPalindrome(n):
	return n == n[::-1]

ans = isPalindrome(n)

if ans:
	print("Palindrom je")
    
else:
	print("Nije palindrom")

isPalindrome(n)


