# guvi
''' Count the no.of.spaces in a given line '''
value = input() 
count = 0
for i in range(len(value)):
  if(value[i]==" "):
    count=count+1
  else:
    continue
print(count)
