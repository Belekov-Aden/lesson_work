#1 Problem
text = input('Введите предложение: ')

def count_text(text):
    zero = 0
    for x in text:
        zero += 1
    print(zero)


count_text(text)


#2 Problem
dictinory_1 = {1:'One'}
dictinory_2 = {2:'Two'}

def accept_dict(*args):
    dictinory_1.update(dictinory_2)
    print(dictinory_1)


accept_dict(dictinory_1, dictinory_2)


#3 Problem menu.txt

def write_menu():
    eat = input('Что хотите покушать?: ')
    drink = input('А что выпить?: ')

    with open('menu.txt', 'w+') as m:
        m.write(f'Ваш заказ: {eat} и {drink}')


write_menu()


#4 Problem get_word
name_file = input('Введите имя файла: ')

def get_word(name_file):
    n = open(name_file, 'w+')
    n.close()


get_word(name_file)


#5 Problem
def general():
    print('Я главная функция')

    def put_in():
        print('Я вложенная')

    put_in()

general()

#6 Problem dict - tuple

dictionary = {1: 'One', 2:'Two', 5: 'dffd', 23: 'sfgdfg'}

def change_type(dict):
    key = tuple(dictionary.keys())
    value = tuple(dictionary.values())
    print(f'Key: {type(key)} {key}\n '
          f'Values {type(value)} {value}')

change_type(dictionary)


#7 Problem easy numbers
def prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return 'Простое число' if counter == 2 else 'Составное число'

print(prime(-2))


#8 Problem
a,b,c = 4,4,8
alll = lambda: a*b*c

print(f'Объём бассейна {alll()} куб')


#9 Problem
from datetime import datetime

dt = datetime.now()
tt = dt.timetuple()

while True:
    year = datetime.now().year  # год текущий
    print(f'Текущая дата: {dt}')
    try:
        day = tt[2]
        month = tt[1]
        start_date = datetime(year, month, day)
        end_date = datetime(year, 12, 31)
    except ValueError as VE:
        print(err)
    else:
        break

print((end_date - start_date).days)
print('осталось дней до нового')


#10 Problem number Fibonachi
def generation_num(num):
    if num < 2:
        print(num)
    else:
        i = 2
        fibo = [0, 1, 1]
        while i <= num:
            fibo[2] = fibo[0] + fibo[1]
            fibo[0] = fibo[1]
            fibo[1] = fibo[2]
            print(fibo[1])
            i += 1


generation_num(10)



#11 Problem labda function

c = lambda x: x * 1.185
print(c(54))


numbers = [1745345, 98726, 439872634, 7312, \
           64872, 123687126, 9312, 4124, 231,\
           3123, 34, 3453]
numbers_1 = []
for i in numbers:
    sum = lambda x: i * 1.185
    numbers_1.append(sum(None).__round__(1))

print(numbers_1)