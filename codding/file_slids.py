#1 exercise
with open('/mnt/c/Users/Lenovo/Desktop/directories.txt', 'w') as f:
	f.write('''bin   dev  home  lib    lib64   lost+found  mnt  proc  run   snap  sys  usr
boot  etc  init  lib32  libx32  media       opt  root  sbin  srv   tmp  var''')

#2 exercise Input log and password
login = input('Введите логин: ')
passwd = input('Пароль: ')
with open('users.txt','w') as w:
	w.write(f'Ваш логин:{login}\n Пароль: {passwd}')

#3 exercise
with open('name.txt', 'r') as r:
    rr = r.read()
    if 'w' in rr:
        print('This here "w"')
    else:
        print('This not here')
#4 execise
with open('python.txt', 'r') as r:
	ree = r.read()
	#w.write('Python is a widely used high-level programming language for general-purpose\
#using whitespace indentation to delimit code blocks rather than curly brackets or\
#keywords), and a syntax that allows programmers to express concepts in fewer lines of\
#code than might be used in languages such as C++ or Java.')
	t_words = []
	for i in ree:
		if i == 't' or i == 'T':
			t_words.append(i)
			print(t_words)


#5 Execise
with open('database.txt', 'r+') as f:
    f_read = f.read()
    f_write = f.write
    login = input('Войти/Зарегистрироваться')
    login = login.upper().lower()
    if login == 'войти':
        login_user = input('Логин: ')
        password_user = input('Пароль: ')
        if login_user and password_user in f_read:
            print('Вы успешно вошли!')
        else:
            print('Неправильные данные')
    if login == 'зарегистрироваться':
        login_user = input('Логин: ')
        password_user = input('Пароль: ')
        if login_user in f_read:
            print('Такой пользователь уже есть!')
        else:
            print(f'Успешно зарегистрировались \n{f.write(login_user)}\n{f.write(password_user)}')