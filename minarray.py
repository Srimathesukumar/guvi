# guvi
''' Minimum element in an arry '''
num=int(input())
arr=input()
l=list(map(int,arr.split(' ')))
min=l[0]
for i in range(1,num):
  if(l[i]<min):
    min=l[i]
print(min)
