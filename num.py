# guvi
''' Count number of numeric digits '''
a=input()
count=0
for i in a:
  if(i.isnumeric):
    count=count+1
print(count)
