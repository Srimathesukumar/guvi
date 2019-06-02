# guvi
''' Count prime number between given range '''
l,r=map(int,input().split())
re = list()
for i in range(l,r+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        re.append(i)
print(len(re))
