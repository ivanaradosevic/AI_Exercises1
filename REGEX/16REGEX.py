#16. Napiši program koji traži određene riječi u stringu:
    #Sample text : 'The quick brown fox jumps over the lazy dog.' 
    # Searched words : 'fox', 'dog', 'horse'

import re
stringac='The quick brown fox jumps over the lazy dog.'

a= re.findall("dog", stringac)
b= re.findall("fox", stringac)
c=re.findall("horse", stringac)
print(a,b,c)

