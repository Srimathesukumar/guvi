# guvi
''' Print lowest and highest number in an array '''
a=int(input())
while(a>0):
  b=input() 
  c=list(map(int,b.split(" ")))
  c.sort() 
  print(c[0],c[-1],end="")
