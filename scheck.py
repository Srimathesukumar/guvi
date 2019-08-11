# guvi
''' Check two strings differ by k characters '''
s1,s2,k=input().split()
l1=list(s1)
l2=list(s2)
print(l1,l2)
k=int(k)
count=0
for i in range(0,len(l1)):
  if(l1[i]!=l2[i]):
    count+=1
    print(count)
if(count==k):
  print('yes')
else:
  print('no')
