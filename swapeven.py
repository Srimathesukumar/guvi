# guvi
''' Swap the even and odd character in a string '''
s=list(input())  
for i in range(0, len(s), 2):
  s[i],s[i+1]=s[i+1],s[i] 
print(''.join(s),end='')
