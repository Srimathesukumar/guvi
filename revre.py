# guvi
''' Remove vowels and print string in reverse '''
a=int(input())
if(a>0):
  string=input()
  rev=string[::-1]
  for i in rev:
    if(i!='a' and i!='e' and i!='i' and i!='o' and i!='u'):
      print(i,end="")
