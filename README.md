# guvi
''' Check the given number is a power of 2 '''
a=int(input())
if(a & (a-1) ==0):
  print('yes')
else:
  print('no')
