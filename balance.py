# guvi
''' Brackets are balanced or not '''
n=input()
l=list(n) 
a=b=0
for i in range(0,len(l)):
  if(l[i]=='('):
    a+=1
  elif(l[i]==')'):
    b+=1
if(a==b):
  print('yes')
else:
  print('no')
