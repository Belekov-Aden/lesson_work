
#Знания на таблицу умножление
num1 = int(input('Первое число:'))
num2 = int(input('Второе число: '))
sum = num1 * num2
answer = int(input('Результат умножения первого числа на второе: '))
if answer == sum:
    print('Верно')
else:
    print(f'Неверно,правильный ответ {sum}')

