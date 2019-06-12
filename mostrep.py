# guvi
''' Print most repeated character in a string '''
a=input() 
k=a[0]
for i in a:
  if(a.count(k)<=a.count(i)):
    k=i
print(k)
