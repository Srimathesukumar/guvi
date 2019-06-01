# guvi
''' Covert Roman to Numerical '''
number=input() 
N=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
if number in N:
  print(N.index(number)+1)
