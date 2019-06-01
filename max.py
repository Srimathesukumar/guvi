# guvi
''' Maximum number among 10 numbers '''
value=list(map(int,input().split()))
max=value[0]
for i in value:
  if(max<i):
    max=i 
print(max)
