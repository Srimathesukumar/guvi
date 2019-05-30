# guvi
''' Count number of special character in a given string '''
value = input() 
count=0
for i in range(len(value)):
  if(value[i].isalpha() or value[i].isdigit() or value[i]==" "):
    continue 
  else:
    count=count+1
print(count)
