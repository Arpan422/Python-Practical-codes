from itertools import combinations
numbers=[]
for i in range (1,10):
    j=int(input('enter no:'))
    numbers.append(j)
c=combinations(numbers,2)
for e in c:
    print(e)           