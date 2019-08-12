# guvi
''' Print the first K characters '''
n,k=input().split()
k=int(k)
a=""
for i in range(0,k):
  a+=n[i]
print(a)
