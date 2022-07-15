#1 Problem
#TypeError
try:
    num = 16
    str_num = '16'
    print(num + str_num)
except TypeError as te:
    str_num = int(str_num)
    print(num+ str_num)

#IndexError
try:
    nums = [1,2,3,4]
    print(nums[5])
except IndexError:
    print('We don`t have this index')
finally:
    print(nums)

#NameError
try:
    print(f'Hello{e}')
except:
    e = 'Aden'
    print(f'Hello {e.upper()}')

#2 Problem
try:

    at = 10
    inn = 15
    wo = 20

    for e in range(-at, at):
        print(wo / e)
        if at > '5':
            print("at > 5")
except TypeError:
    print('Bad')

#3 Problem
try:
    lst = []
    for i in range(10):
        lst.append(i)

    a = list(reversed(lst))
    sls_obj = slice('0','8')
    print(a[sls_obj])
except TypeError:
    sls_obj = slice(0, 8)
    print(a[sls_obj])

#4 Problem
a = (0)
b = (1)
numbers = []
while b > a:
    numbers.append(b)
    b += 1
    print(b)
    if b == 10:
        break
