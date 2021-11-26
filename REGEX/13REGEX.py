#13. Napiši program koji miče nule iz IP adresa

import re
adress="755.023.156.008"
ip = re.sub('0', '', adress)
print(ip)