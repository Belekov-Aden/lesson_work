#1 Problem
values = ("TURUSBEKOVA 109/1", 10, 1005, ["TABLES", "CHAIRS"], 23.00)

def my_func(val):
  try:
    set(val)
  except:
    return False
  else:
    return True

my_func(values)


my_list = list(map(my_func, values))
print(my_list)

if all(my_list):
  print("Мы можем конвертировать")
else:
  print("Мы не можем")


#2 Problem
def user_input_add():
    for i in range(5):
        numbers = int(input(f'Число №: '))
        if i == 0:
            numbers_set = set()
            numbers_set.add(numbers)
        elif i == 1:
            numbers_set.add(numbers)
        elif i == 2:
            numbers_set.add(numbers)
        elif i == 3:
            numbers_set.add(numbers)
        elif i == 4:
            numbers_set.add(numbers)

            print(numbers_set)

    print(f'Самое максимальное значение: {max(numbers_set)}\n'
f'И самое наименьшее число {min(numbers_set)}')
user_input_add()

#2 Problem other
def user():
    num = [int(input('введите число: '))for num in range(5)]
    print(set(num))
    print(f'И самое наименьшее число {min(num)}')
user()


#3 Problem
def do_function_python():
    function_python = input('Ввод функций python: ')
    try:
        eval(function_python)
    except:
        False
        print('Функция невыполнима')
    else:
        True
        print('Функция выполнима')


do_function_python()


#4 Problem
loan = int(input('Сумму займа: '))
if loan < 50_000:
    print('Не меньше 50 000 !')
else:
    def count_loan():
        global percent
        percent = 3.47
        return_loan = loan * (percent / 100)
        sum = loan + return_loan
        print(f'Вам нужно вернуть {sum.__round__(2)}')

    count_loan()