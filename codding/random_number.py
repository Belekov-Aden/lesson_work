from random import randint
numbers = randint(0 ,100)
numbers_input = int(input('Отгадайте число: '))

for x in range(10):
    if numbers > numbers_input:
        print('Ваше число меньше')
        if numbers <