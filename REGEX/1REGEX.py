#1. Napiši program koji provjerava sadrži li string određeni set charactera.
#    a) a-z 
#    b) A-Z 
#    c) 0-9

import re 
txt="a,b,c,d,e,f,g,1,2,3,4,ABCDEFGH"
x =bool(re.findall("[a-z]", txt))  #mogu ispred staviti bool da provjrim sadrzi li ta slova/True or False
y=bool(re.findall("[A-Z]", txt))
w=bool(re.findall("[0-9]",txt))


print(x)
print(y)
print(w)


