#Calculator

sign = '1'

while True:
    if sign == '0':
        print('Операция завершена!')
        break
    num_1 = float(input('Число: '))
    num_2 = float(input('Число: '))
    sign = input('Операция: +/-* ** ')

    if sign == '+':
        print(num_1 + num_2)

    elif sign == '-':
        print(num_1 - num_2)

    elif sign == '*':
        print(num_1 * num_2)

    elif sign == '/':
        try:
            if num_2 == 0:
                print('На ноль делить нельзя')
            print(num_1 / num_2)
        except ZeroDivisionError:
            pass

    elif sign == '**':
        print(num_1 ** num_2)