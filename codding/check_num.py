#Проверка чила в консоли
number = int(input('Введите число: '))

if number < 10:
    print('Меньше 10')
elif number >= 10 and number < 100:
    print('Число в промежутке между 10 и 100')
else:
    print('Число больше 100')