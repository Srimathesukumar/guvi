# guvi
''' vowel or consonent '''
import re
value=input()
symbol=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
if(symbol.search(value)==None):
  if(value=='a'or value=='e'or value=='i'or value=='o'or value=='u'):
    print('Vowel')
  else:
    print('Consonant')
else:
  print('invalid')
