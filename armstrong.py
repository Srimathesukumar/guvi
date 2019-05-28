# guvi
''' Armstrong number or not '''
number=int(input())
temp=number
count=0
while(number > 0):
   digit = number % 10
   count += digit ** 3
   temp //= 10

# display the result
if(temp==count):
   print("yes")
else:
   print("no")
