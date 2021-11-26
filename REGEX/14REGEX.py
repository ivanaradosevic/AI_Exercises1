#14. Napiši program koji traži postoji li broj na kraju stringa
import re
stringac= "miškomalitrazibroj3heheheheh6"
xac=re.findall("[0-9]$", stringac)
print(xac)