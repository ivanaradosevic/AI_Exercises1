#10. Napiši program koji vraća zadnju riječ u stringu, zajedno s opcionalnim punktuacijama

import re
stringac="abbcbd a0befgh abbbbjhkjh a2Babaaaaaaa!"
x = re.findall(r"\w+.\Z", stringac)
print(x)