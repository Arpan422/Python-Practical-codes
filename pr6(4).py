n=int(input('how many elemens required for list:'))
first=[]
for i in range(1,n+1):
    first.append(int(input('enter element:')))
print(first)
c=[]
for ii in first:
    if i not in c:
        c.append(i)
print(c)