import math
pi=3.14
height=int(input("please enter the height of the ladder:"))
deg=int(input("please enter the angle of the ladder in degrees:"))
rad=(pi/180)*deg
leng=height/(math.sin(rad))
print("the length of the ladder must be",leng)