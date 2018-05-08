import random
num = int(input('Number of times to flip coin: '))
flips = [random.randint(0,1) for r in range(num)]
results = []
for object in flips:
        if object == 0:
            results.append('Heads')
        elif object == 1:
            results.append('Tails')
print(results)
print('you got '+str(results.count("Heads"))+' heads and '+str(results.count("Tails"))+' tails')
