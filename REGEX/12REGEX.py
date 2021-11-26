#12. Napiši program koji provjerava i vraća rezultat ako se u stringu pojavljuju samo velika i mala slova,
 #brojevi i underscore.

import re
stringac="Ab555_Bcbd Abefgh abb_jhkjh a2Bab_aa_aaaaa malaslova!"
x = re.findall(r"\w+_\w+", stringac)
print(x)

"""import re
a= "mdlskdksandkasfnKKK_KHGggjhjhbqjhd"   
b="ddčjhjhjjdhdjhhshssj"

if re.search('^[a-zA-Z0-9_]*$', b):
    print("dobro je")
else:
    print("nije dobro")
"""

