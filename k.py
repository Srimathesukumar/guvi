# guvi
''' Sum of first 'k' integer '''
number = input()
number = number.split()
N = int(number[0])
K = int(number[1])
array = list(map(int,input().strip().split()))[:N] 
add = 0
for i in range(0,K):
  add = add+array[i]
print(add)
