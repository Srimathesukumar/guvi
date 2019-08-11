# guvi
''' Encoded string by adding 3 in each character '''
n=input()
a=list(n)
l=['A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
b=[]
for i in range(0,len(a)):
  for j in range(0,len(l)):
    if n[i] in l[j]:
      b.append(l[j+3])
print("".join(b))
