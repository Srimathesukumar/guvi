# guvi
''' Print the array after right shift K times '''
n,k=input().split()
n=int(n)
k=int(k)
arr=list(map(int,input().split()))[:n]
k=k%n
l=arr[-k:]+arr[:-k]
print(*l)
