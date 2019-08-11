# guvi
''' check k value present in sorted array or not '''
n,k=map(int,input().split())
arr=list(map(int,input().split()))[:n]
c=0
for i in range(0,len(arr)):
  if(arr[i]==k):
    c+=1
if(c==0):
  print('no')
else:
  print('yes')
