# guvi
''' Convert upper to lower and viceverse '''
n=input() 
a=list(n)
b=[]
for i in range(0,len(a)):
  if(a[i].isupper()):
    b.append(a[i].lower())
  else:
    b.append(a[i].upper())
print(''.join(b))
