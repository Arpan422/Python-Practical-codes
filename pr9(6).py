a=3
b=2
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def square(a):
    return a*a
def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
print("value of a =",a)
print("value of b =",b)
print("addition of a,b is:",a+b)
print("subtraction of a,b is:",a-b)
print("multiplication of a,b is:",a*b)
print("division of a,b is:",a/b)
print("modulus of a,b is:",a%b)
print("square of a is:",a*a)
print("factorial of a is:",a*factorial(a-1))