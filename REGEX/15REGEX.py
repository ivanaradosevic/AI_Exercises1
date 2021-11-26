#15. Napiši program koji traži dvoznamenkaste i troznamenkaste brojeve (0-9) u bilo kojem stringu.
import re
stringac="1dvoznamenkasti22itroznamenkasti333stringaci"
xac=re.findall(r"[0-9]{2,3}", stringac)
print(xac)