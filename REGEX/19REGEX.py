#19. Napiši program koji izbacuje samo brojeve iz nekog URL-a.

import re
stringac= "https//www.hdkewhfkeahfk876.com/index.html"
xac= re.sub("[0-9]", "", stringac)
print(xac)
