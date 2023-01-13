p=int(input('enter principle amount:'))
n=int(input('enter no of year:'))
r=int(input('enter rate of intrest:'))
si=p*r*n/100
print('simple intrest=',si)
t=int(input('enter number of year elapsed:'))
ci=p*pow(1+(r/100*n),(n*t))
print('compound intrest',ci)