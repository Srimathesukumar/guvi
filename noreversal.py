# guvi
''' Number reversal '''
number = int(input())
sum=0
while(number>0):
  digit=number%10
  sum=(sum*10)+digit
  number=number//10
print(sum)
