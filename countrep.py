# guvi
''' Print the occurance of K in N '''
n,k=input().split()
a=list(n)
k=int(k)
c=0
for i in range(0,len(a)):
  if(int(a[i])==k):
    c+=1
print(c)
