# guvi
''' Count the no.of.characters in string without counting the space '''
value = input() 
count = 0
for i in range(len(value)):
  if(value[i]==" "):
    continue
  count=count+1
print(count)
