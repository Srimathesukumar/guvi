# guvi
''' Print the longest common prefix '''
value=int(input())
list1=[]
for i in range (0,value):
    m=input()
    list1.append(m)
list2=[]   
for j in zip(*list1):
	if j.count(j[0])==len(j):
		list2.append(j[0])
	else:
		break
print(''.join(list2))
