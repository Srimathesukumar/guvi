# guvi
''' Check for the K value in given list '''
N,K=map(int,input().split())
arr=list(map(int,input().split()))[:N]
b=False
for i in range(0,len(arr)):
  if(arr[i]==K):
    b=True
if(b==True):
  print('yes')
else:
  print('no')
