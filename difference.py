# guvi
'''  Two times in hr:min format subtract '''
t1,t2 = input().split()
h1,h2 = input().split()
t1 = int(t1)
t2 = int(t2)
h1 = int(h1)
h2 = int(h2)
time1 = (t1*60)+t2
time2 = (h1*60)+h2
if(time1 > time2):
  result=time1-time2
else:
  result=time2-time1
hour=0
if(result<=59):
  print(hour,result)
else:
  while(result>59):
    result=result-60
    hour=hour+1
  print(hour,result)
