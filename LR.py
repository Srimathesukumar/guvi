# guvi
''' Print the Smallest number divisible by L & R '''
L,R=input().split()
L=int(L)
R=int(R)
for i in range(1,10000):
  if(i%L==0 and i%R==0):
    print(i)
    break
