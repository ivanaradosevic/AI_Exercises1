#9. Napiši program koji će provjeravati postoji li u stringu 'a'
# iza kojega slijedi bilo što i da završava na 'b'.

import re
stringac="abbcbd a0befgh abbbbjhkjh a2Babaaaaaaa"
x = re.findall(r"a\w+b", stringac)
print(x)