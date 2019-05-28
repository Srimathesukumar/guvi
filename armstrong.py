# guvi
''' Armstrong number or not '''
number=int(input())
temp=number
count=0
while(temp > 0):
   digit = temp % 10
   count += digit ** 3
   temp //= 10

# display the result
if(nmuber==count):
   print("yes")
else:
   print("no")
