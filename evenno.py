# guvi
''' Print even number between interval '''
N,Q = input().split()
N=int(N)
Q=int(Q)
for i in range(N+1,Q):
  if(i%2==0):
    print(i,end=" ")
  i+=1
