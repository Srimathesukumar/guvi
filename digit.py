# guvi
''' Print Sum of all its digit '''
n=input()
l=list(n)
s=0
for i in range(0,len(l)):
  s=s+int(l[i])
print(s)
