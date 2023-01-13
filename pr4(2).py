hrs=float(input("enter hours:"))
rate=float(input("enter the rate:"))
if hrs<=40:
    print(hrs*rate)
elif hrs>40:
    print("Total wages of the weak=",40*rate+(hrs-40)*1.5*rate)