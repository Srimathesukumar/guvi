# guvi
''' Print no.of repetitions of K '''
N,K=map(int,input().split())
arr=list(map(int,input().split()))[:N]
c=0
for i in range(0,len(arr)):
  if(arr[i]==K):
    c+=1
print(c)
