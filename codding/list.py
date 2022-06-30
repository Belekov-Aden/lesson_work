#Problem #1
aden = [1, 1.0, 'Aden', True, [2,3,4,5]]
print(type(aden[0]))
print(type(aden[1]))
print(type(aden[2]))
print(type(aden[3]))
print(type(aden[4]))

#Problem2
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon',\
         'Jackson', 'Jhon',  'Jimmy', 'Jackson', \
         'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson',\
         'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]

print(names.count('Jack'))

#Problem 3
#Удалить все четные индекса до 10
print(len(names))
new_name = names[:11]
del new_name [1::2]
print(new_name)

#Problem 4
my_information = []
my_information.append(input('Как вас зовут?:  '))
my_information.append(int(input('Год вашего рождения?:  ')))
my_information.append(input('Любимый язык программирования?:  '))
print(my_information)

#Problem 5
en_names = ['Aden', 'Deniz', 'Dastan', 'Ailina', 'Sari']
print(''.join(en_names))




