# guvi
''' Check given array in sorted order '''
n=int(input())
a=list(map(int,input().split()))[:n]
if(a==sorted(a)):
  print('yes')
else:
  print('no')
