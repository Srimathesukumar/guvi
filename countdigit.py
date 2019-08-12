# guvi
''' Count number of digits of an integer '''
n=input()
a=list(map(int,n))
c=0
for i in range(0,len(a)):
  c+=1
print(c)
