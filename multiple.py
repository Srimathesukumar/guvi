# guvi
''' Multiples of 1st five 'N' numbers '''
num=int(input())
product=1
for i in range(1,6):
  product=num*i 
  print(product,end=" ")
