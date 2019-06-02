# guvi
''' Check two strings will be differ by one character '''
s1,s2=map(str,input().split())
count=0
for i in range(0,len(s1)):
  if(s1[i]!=s2[i]):
    count=count+1
  else:
    continue
if(count==1):
  print('yes')
else: 
  print('no')
