# guvi
''' Print GCD of given number '''
a,b=map(int,input().split())
if(a>b):
  s=b
else:
  s=a
for i in range(1,s+1):
  if(a%i==0 and b%i==0):
    c=i
print(c)
