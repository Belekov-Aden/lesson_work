
#0 Problem
dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
print(dates_of_birth)

#1 Problem
age = {1,2,3}
translate = {'One', 'Two', 'Three'}
date = {2022}

our = set.union(age, translate, date)
print(type(our))
print(our)

#2 Problem
#Во множестве №2 найдите объекты которых нет во множестве №1
farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

farm_our = set.symmetric_difference(farm_1, farm_2) #Разница обоих множест
print(farm_our)

farm_our_1 = set.difference(farm_2,farm_1) #Разница множества №2 в №1
print(farm_our_1)
#3 Problem

num = {1,2,3,4,5}
print(num)
num.add(6)
print(num)
num.pop()
print(num)

num = set('HelIo')
print(num)
num.add('Go')
print(num)
num.pop()
print(num)

for x in range(10):
    num_10 = int(input('Введите число: '))
    fronz_num = frozenset()
    fronz_num.add(num_10)
    print(type(fronz_num))