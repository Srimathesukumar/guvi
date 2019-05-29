# guvi
''' Print time in hours and minutes '''
min = int(input())
hrs = 0
if(min<=59):
  print(hrs,min)
else:
  while(min>59):
    min=min-60
    hrs=hrs+1
  print(hrs,min)
