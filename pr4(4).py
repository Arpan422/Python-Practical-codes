from re import A


sub1=int(input("enter marks of first subject:"))
sub2=int(input("enter marks of second subject:"))
sub3=int(input("enter marks of third subject:"))
sub4=int(input("enter marks of fourth subject:"))
sub5=int(input("enter marks of fifth subject:"))
avg=(sub1+sub2+sub3+sub4+sub5)/5
print("percentage=",avg)
def switch():
    if(avg>=90):
        print("grade:a")
    elif(avg>=80 and avg<90):
        print("grade:b")
    elif(avg>=70 and avg<80):
        print("grade:c")
    elif(avg>=60 and avg<70):
        print("grade:d")
    elif(avg>=50 and avg<60):
        print("grade:e")
    else:
        print("grade:f")
    switch()
        