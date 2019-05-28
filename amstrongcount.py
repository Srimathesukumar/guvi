# guvi
N,Q=input().split()
N=int(N)
Q=int(Q)
for i in range(N,Q):
  count=0
  a=len(str(i))
  temp = i
  while(temp> 0):
   digit = temp % 10
   count += digit ** int(a)
   temp //= 10
  if(i==count):
   print(i,end="")
