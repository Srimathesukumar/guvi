# guvi
''' Fibonacci series of N number '''
number=int(input())
a=0
b=1
for num in range(1,number+1):
  if(num<=1):
     next=num
  else:
    next=a+b
    a=b
    b=next
  print(next,end=" ")
