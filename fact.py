# guvi
''' Factroial of a number '''
num = int(input())
sum=1
if(num<=20):
  for i in range(1,num+1):
    sum=sum*i
  print(sum)
