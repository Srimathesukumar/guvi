# guvi
''' Swapping two number using bitwise operator '''
number = input() 
number = number.split() 
n1 = int(number[0])
n2 = int(number[1])
n1=n1^n2
n2=n1^n2
n1=n1^n2
print(n1,n2)
