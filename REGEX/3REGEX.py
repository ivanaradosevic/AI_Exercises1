#3. Napiši program koji će provjeravati postoji li u stringu 'a' 
# iza kojeg se nalazi jedno ili više 'b'

import re
stringac="abcbd0efgh ajhkjh aBabaaaaaaa"
x = re.findall("ab+", stringac)
print(x)