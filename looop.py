#!/usr/bin/python3
'''
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
'''

numbered_dogs={}
dogs =["kanich","bergi","pitbull","chiwawa"]

i=1
for dog in dogs:
	new_dog_name= ' %s' % dog
	numbered_dogs[new_dog_name] = new_dog_name+str(i)	
	i=i+1

#.value to retrieve only value for name in numbered_dogs.values()
# .items to retrieve names and values
for name, value in numbered_dogs.items():
	print(name)


