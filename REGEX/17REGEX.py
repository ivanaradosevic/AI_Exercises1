#17. Za svaku riječ iz zadatka 16. izbaci i od kojeg do kojeg indeksa se pojavljuju
import re
stringac='The quick brown fox jumps over the lazy dog.'

a= re.search("dog", stringac)
b= re.search("fox", stringac)
c=re.search("horse", stringac)
print(a,b,c)
