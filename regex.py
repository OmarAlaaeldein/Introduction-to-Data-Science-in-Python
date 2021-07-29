import re
#use ternary operators
x=0
print('1') if x==1 else print('False')
#use search to find word in text
s='very good morning'
print('found') if re.search('good',s) else print('not found')
#segmant a string based on character or word
ss="Amy is great, Amy is wholesome"
print(re.split('Amy', ss))
#count repetition of a patern in a string
print(re.findall("Amy", ss))
#Anchors de