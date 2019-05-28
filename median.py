# guvi
''' Median value in an array '''
num=int(input())
arr=input()
l=list(map(int,arr.split(' ')))
l.sort()
if num % 2 == 0: 
    median1 = l[num//2] 
    median2 = l[num//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = l[num//2] 
print(median) 
