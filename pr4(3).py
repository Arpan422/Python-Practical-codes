weight=int(input('enter weight:'))
height=float(input('enter height:'))
bmi=weight/(weight*height)
print('bmi=',bmi)
if bmi>=19 and bmi<=25:
    print('healthy')
elif bmi>25:
    print('overweight')
else:
    print('underweight')