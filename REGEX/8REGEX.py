#8. Napiši program koji traži sequence velikih slova iza kojih se nalaze mala slova.

import re
stringac= "MMMalihslova Ima Ovdje NNNNNekoliko i Sada Ce ih Naci"
x=re.findall(r"[A-Z]{2,}[a-z]", stringac)
print(x)
