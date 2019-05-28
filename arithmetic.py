# guvi
''' Sum of Arithmetic progression '''
N,A,D=input().split()
N=int(N)
A=int(A)
D=int(D)
sum = 0
i = 0
while (i<N): 
  sum = sum + A 
  A = A+D
  i+=1
print(sum)
