#9. Napišite algoritam koji prima nasumičan pozitivni broj manji od 86400 te pretvara taj broj iz 
# sekunda i ispisuje koliko je to točno vrijeme u satima, minutama i sekundama

import random
import datetime
a= random.randint(0 , 86400)
conv = str(datetime.timedelta(seconds=a))
print(f"{a} sekunda je: {conv}")

