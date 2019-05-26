# guvi
''' Largest of three number '''
number = input()
number = number.split()
num1 = int(number[0])
num2 = int(number[1])
num3 =int(number[2]) 
if(num1>num2 and num1>num3):
  print(num1)
elif(num2>num1 and num2>num3):
  print(num2)
elif(num3>num1 and num3>num2):
  print(num3)
elif(num1==num2 and num2==num3):
  print(num1)
elif(num1==num2):
  print(num1)
elif(num2==num3):
  print(num2)
else:
  print(num3)
