# guvi
''' Print average of n number '''
n=int(input())
while(n>0):
  v=list(map(int,input().split()))
  sum=0
  for i in range(0,n):
    sum=sum+v[i]
  print(sum//n)
