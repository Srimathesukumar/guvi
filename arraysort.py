# guvi
''' Improved input constrain sorting ''' 
num=int(input())
arr=input()
l=list(map(int,arr.split(' ')))
l.sort()
if(num<=100000):
  for i in l:
    print(i,end=' ')
