n=int(input('how many fibonnaci numbers do you want?'))

f1=1

f2=1

if n<0:

  print ('you can not have negative amounts of fibonacci numbers')

elif n<2:

  print (n)

elif n>=2:

  print ("1\n1")

for num in range(2,n):

  f2=f1+f2
  f1=f2-f1

  print (f2)