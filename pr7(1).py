#Create a tuple with different data types.
tuple1=(10,20,30,40,50)
print(tuple1)
#Print tuple items.
for i in tuple1:
 print(i)
#Convert tuple into a list.
 lst = list(tuple1)
#print list
print(lst)
print(type(lst))
#Remove data items from a list.
lst.remove(50)
print(lst)
#Convert list into a tuple.
tpl=tuple(lst)
print(type(tpl))
#Print tuple items.
print(tpl)