#21. Napišite funkciju koja prima isključivo stringove i vraća tuple pojedinačnih charactera, 
#uključujući i razmake.

n=input("unesi nešto:")
def funk(n):
    m=str(n)
    lista=[]
    for i in m:
        lista.append(i)
    t=tuple(lista)
    print(t)

funk(n)
    