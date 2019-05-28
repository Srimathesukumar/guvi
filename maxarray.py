# guvi
''' Maximum element in an array '''
num=int(input())
arr=input()
l=list(map(int,arr.split(' ')))
max=l[0]
for i in range(1,num):
  if(l[i]>max):
    max=l[i]
print(max)
