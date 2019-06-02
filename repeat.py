# guvi
''' Print the repeated number in sorting order '''
N=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
  if(a.count(i)>1):
    b.append(i)
c=set(b)
if(len(c)==0):
  print('unique')
else:
  print(*c)
