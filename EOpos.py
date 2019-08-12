# guvi
''' Print even no's in even position and odd no's in odd position '''
N=int(input())
arr=list(map(int,input().split()))[:N]
a=False
for i in range(0,len(arr)):
  if(i%2==0 and arr[i]%2==0):
    a=True
  elif(i%2!=0 and arr[i]%2!=0):
    a=True
  else:
    print(arr[i],end=" ")
