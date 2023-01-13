year=int(input('enter year:'))
if year%400==0 and year%4==0:
    print('century leap year')
elif year%100==0:
    print('century year')
elif year%4==0:
    print('leap year')
else:
    print('not leap year')