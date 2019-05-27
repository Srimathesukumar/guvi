# guvi
''' Prime number or not '''
value=int(input())
if(value>0):
  for i in range(2,value//2):
    if(value%i==0):
      print('no')
      break
  else:
    print('yes')
else:
  print('no')
