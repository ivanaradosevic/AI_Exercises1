#18. Pronađi sve substringove 'exercises' u 'Python exercises, PHP exercises, C# exercises'

import re
stringac= "Python exercises, PHP exercises, C# exercises"
xac=re.findall("exercises", stringac)
print(xac)