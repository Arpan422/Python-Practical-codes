def emi_calculator(p,r,t):
    r=r/(12*100)
    t=t*12
    emi=(p*r*pow(1+r,t))/(pow(1+r,t)-1)
    return emi
principal=10000;
rate=10;
time=2;
emi=emi_calculator(principal,rate,time);
print("Monthly EMI is=",emi)