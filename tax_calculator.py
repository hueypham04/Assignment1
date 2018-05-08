import sys
a=float(sys.argv[1])
if a<0:
  print ('you cannot be taxed for negative earnings, enter a positive value')
elif a<18200:
  print(0)
elif a<37000:
  print ((a-18200)*0.19)
elif a<87000:
  print (3572 +(a-37000)*0.325)
elif a<180000: 
  print (19822 +(a-87000)*0.37)
elif a>180000:
  print (54532 +(a-180000)*0.45)