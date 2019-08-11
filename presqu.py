# guvi
''' Count prefect squares in given range '''
a,b=map(int,input().split())
count=0
for i in range(a,b+1):
  j=1
  while(j*j<=i):
    if(j*j==i):
      count+=1
    j+=1
  i+=1
print(count)
