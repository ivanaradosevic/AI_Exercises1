#6. Napiši program koji će provjeravati postoji li u stringu 'a' iza kojeg se nalazi 2 do 3 'b'

import re
stringac="abbcbd0efgh abbbbjhkjh aBabaaaaaaa"
x = re.findall("ab{2,3}", stringac)
print(x)