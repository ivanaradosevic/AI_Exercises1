#4. Napiši program koji će provjeravati postoji li u stringu 'a' 
# iza kojeg se nalazi jedno ili dva 'b'

import re
stringac="abbcbd0efgh abbbbjhkjh aBabaaaaaaa"
x = re.findall("ab{1,2}", stringac)
print(x)