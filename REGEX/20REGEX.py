#20. Prebaci format datuma iz našeg u američki.

import re
datum= "26.11.2021"
xac=re.sub(r"(\d{1,2}).(\d{1,2}).(\d{4})", r'\2-\1-\3',datum)
print(xac)
