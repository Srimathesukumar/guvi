# guvi
''' Print Prime Factors in Sorted order '''
N=int(input())
l=[]
b=True
for i in range(2,N+1):
  if(N%i==0):
    l.append(i)
for i in range(2,len(l)):
  for j in range(2,i):
    if(i%j==0):
      b=False
  if b is True:
      print(i,end=" ")
