#11. Napiši program koji vraća sve riječi koje sadrže 'z'

import re
stringac="abbcbd a0bzefgh abbbbzjhkjh a2Babaazaaaaa!"
x = re.findall(r"\w*z\w*", stringac)
print(x)