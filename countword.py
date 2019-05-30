# guvi
''' Count the no.of.words in given line '''
value = input() 
a=0
b=1
state=a
wordcount = 0
for i in range(len(value)):
  if(value[i]==" "):
    state=0
  elif(state==a):
    state=b
    wordcount=wordcount+1
print(wordcount)
