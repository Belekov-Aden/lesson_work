#1 Problem
#Метод первый вручную
list_1 = ['name', 'age', '1', '19']

first = list_1[:2]
second = list_1[-2::]

first[-1], first[0] = first[0], first[-1]
second[-1], second[0] = second[0], second[-1]

new_list = first + second
print(new_list)
print(first)
print(second)


l = ['name', 'age', '1', '19']


def reverse_list(list):
    l1 = l[1::-1]
    l2 = l[:-3:-1]
    print(l1 + l2)


reverse_list(l)


# 2 Problem Recurse in Fibonachi
def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n-1) + fibonacci(n-2)
    return cur

element = input('Введите номер искомого элемента : ')
element = int(element)
value = fibonacci(element)
print(value)

#3 Problem call function
numbers = int(input('Введите первое число:'))
numbers_2 = int(input('Введите второе число:'))

def call():

    def additions(numbers, numbers_2):
        sum = numbers + numbers_2
        print(f'При сложении этих чисел = {sum}')


        def subtraction(numbers, numbers_2):
            sum_s = numbers - numbers_2
            print(f'А при вычитании = {sum_s}')

        subtraction(numbers, numbers_2)

    additions(numbers, numbers_2)

call()

#4 Problem

user = input('Name file: ')

def create():
    with open(user, 'w+') as f:
        f.write('I write this through Python function')

call = create()
print(call)


#5 Problem function generation number
import random

def gen_number():
    a = ['0444',str(random.randint(100_000, 900_000))]
    out_a = ''.join(a)
    print(out_a)

gen_number()

#6 Problem odd numbers Recursion

def odd_print():
    for i in range(20):
        if i % 2 == 1:
            print(i)


odd_print()

#7 Problem get Recursion

a = {1,2,3,4,5,5,7,7}
print(a)
def get_set(set):
   while True:
       if a == set:
           try:
               a.pop()
               print(a)
           except KeyError:
               pass

get_set(a)