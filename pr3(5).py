a=int(input('enter No1:'))
b=int(input('enter No2:'))
c=int(input('enter No3:'))
max=(a if(a>b and a>c)else
     (b if(b>a and b>c)else c))
print('maximum number is',max)