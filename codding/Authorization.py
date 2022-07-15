
#Authorization
login = input('Введите логин: ')
password = input('Введите пароль: ')

print(f'Для входа введите заранее придуманный логин и пароль')
log = input('Логин:')
pas = input('Пароль: ')
if login == log and password == pas:
    print('True')
else:
    print('False')