# guvi
''' Check given number is power of 2 or not '''
n=int(input())
a=True
if(n==0):
  a=False
while(n!=1):
  if(n%2!=0):
    a=False
  n=n//2
if(a==False):
  print('no')
else:
  print('yes')
