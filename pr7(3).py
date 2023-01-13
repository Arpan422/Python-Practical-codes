#Create a dictionary.
person={'name':'dhara','age':32,'salary':37000}
print(type(person))
#Print dictionary items.
print("Name:",person['name'])
print("Age:",person['age'])
print("salary:",person['salary'])
#Add/remove key-value pair in/from a dictionary.
edict={}
print('empty dictionary')
print(edict)
edict[0]="pinky"
edict[1]="dhara"
print(edict)
del edict[0]
22
print(edict)
'''del edict
print(edict)'''
#Check whether a key exists in a dictionary.
key1=input('Enter Key name')
if key1 in person.keys():
 print('key is in dictionary')
else:
 print('key is not in dictionary')
#Iterate through a dictionary.
employee={'name':'dhara','age':32,'salary':37000}
for x in employee:
 print(x)
for x in employee.values():
 print(x)
for x in employee.items():
 print(x)
for x,y in employee.items():
 print(x,y)
#Concatenate multiple dictionaries.
person.update(edict)
print(person)
