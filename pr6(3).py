string=input('enter string:')
i=0
c=[]
while i<len(string):
    if string[i]not in c:
        c.append(string[i])
        if string[i].isdigit():
            a=string.count(string[i])
            print(string[i],a,'time')
    i+=1