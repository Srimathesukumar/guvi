# guvi
''' Count number of numeric in a given string '''
value = input() 
count=0
for i in value:
  if(i.isdigit()):
    count=count+1
print(count)
