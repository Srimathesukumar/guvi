# guvi
''' vowel or consonent '''
import re
value=input()
symbol=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(symbol.search(value)==None):
  if(value==('a' or 'e' or 'i' or 'o' or 'u')):
    print('Vowel')
  else:
    print('Consonant')
else:
  print('invalid')
