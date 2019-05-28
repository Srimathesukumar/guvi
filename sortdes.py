# guvi
''' Sorting an element in an array '''
num=int(input())
arr=input()
l=list(map(int,arr.split(' ')))
l.sort()
for i in l:
  print(i,end=' ')
