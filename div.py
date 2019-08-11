# guvi
''' Check if N is divisible by any number less than N other than 1 '''
n=int(input())
a=False
for i in range(2,n):
  if(n%i==0):
    a=True
if(a==True):
  print('yes')
else:
  print('no')
