#Problem №1
term_1 = 2 ** 3
term_2 = 3 ** 2

if term_1 > term_2:
    print('2 ** 3 больше')
else:
    if term_2 > term_1:
        print('3 ** 2 больше')
    else:
        print()

#Problem №2
integer_1 = int(input('Введите первое число:'))
integer_2 = int(input('Введите второе число:'))
integer_3 = int(input('Введите третье число:'))


if integer_1 > integer_2 and integer_1 > integer_3:           #Определяем самое большое число
    print('Первое число больше!')
else:
    if integer_2 > integer_1 and integer_2 > integer_3:
        print('Второе число больше!')
    else:
        if integer_3 > integer_2 and  integer_3 > integer_1:
            print('Третье число больше!')

if integer_1 < integer_2 and integer_1 < integer_3:           #Определение самого наименьшего числа!
    print('Первое число меньше!')
else:
    if integer_2 < integer_1 and integer_2 < integer_3:
        print('Второе число меньше!')
    else:
        if integer_3 < integer_2 and  integer_3 < integer_1:
            print('Третье число меньше!')

#Problem 3
first = 17391
second = 546
third = 934

if first % 17 <= 0:
    print('17391 остаток меньше всего')
else:
    if second % 17 <= 0:
        print('546 остаток меньше всего')
    else:
        if third % 17 <= 0:
            print('934 меньше всего остаток')
        else:
            print('Error')

#Problem 4

x = 13 ** 2

if x > 172:
    print('13 в квадрате > 172')
else:
    if x ** 2 > 172:
        print('13 в кубе больше 172')
    else:
        print('')

#Promlem 5
a = int(input('Введите число для проверки(четности-деление без остатка-больше ли это число в квадрате 1000 ?) : '))
if a % 2 == 0:
    print('Число четное!')
else:
    print('Число нечетное!')

if a % 3 == 0:
    print('Число делится на 3 без остатка')
else:
    print('Число делится на 3  с остатком')

if a ** 2 > 1000:
    print ('Больше')
else:
    print('Не больше')


#Problem 6

one_hundred = int(input('От 0 - 100:'))

if one_hundred >= 0 and one_hundred <= 21:
    print('Число разрешен!')
else:
    if one_hundred >= 57 and one_hundred == 100:
        print('Число разрешен!')
    else:
        print('Число не разрешен!')

#Porblem 7
if True:
    print('Always')

#Problem 8
age = int(input('Введите возраст: '))
if 12 >= age  or 18 >= age  or 24 >= age:
    print('Вы молодой еще!')
else:
    print('Вы старый!')

#Problem 9
a = 10 // 5
b = 10 / 5
if a == b:
    c = a + b
    print('Они равны и их сумма', c )
else:
    print('Они не равны')

#Problem 10
full_name = int(input('Ввести число!'))
if full_name < 0:
    print('Правильно')
else:
    print('Ввести отрицательное число')

#Problem 11
peremennay_1 = 10
peremennay_2 = 5
if peremennay_1 >= 0 and peremennay_2 >= 0:
    print('Числа положительные!')

#Problem 12
if peremennay_1 > peremennay_2:
    print(peremennay_1 + 2)

else:
    print(peremennay_2 + 2)


