#Задание слайдов for / while

#Первое задание 1
languages_1 = input('Язык программирование: ')
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for l in languages:
    if l == languages_1:
        print(f'This languages is in list {l}')

if lang1 == languages_1:
    print(f'This languages is in list {lang1}')

#Second work 2
for l in languages:
    if l == 'php':
        break
    print(l)

#Third work 3
number = 7
for ii in range(5):
    number = number * 7
    print(number)

#Forth work
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

for aa, lan in enumerate(languages):
    print(aa + 1, lan)

#Fifth work
zero = 10
zo= 0
while zo < 10:
    zo += 1
    print(zo, end=',')
for i in range(zero):
    zero -= 1
    print(zero, end=',')



