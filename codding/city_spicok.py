#City список

city = ['1. Добавить новый город',
'2. Отобразить список городов',
'3. Заменить город',
'4. Удалить город',
'5. Выход']
print('\n'.join(city))


answer = int(input('Выберите действие: '))
if answer == 1:
    new_city = []
    name_city = input('Введите название города:')
    new_city.append(name_city)
    print('Город добавлен')
else:
    print(f'Такой город уже есть! {name_city}')


print('\n'.join(city))
answer = int(input('Выберите действие: '))

    if answer == 2:
        print(f'Список городов: \n{new_city}')
    else:

print('\n'.join(city))
answer = int(input('Выберите действие: '))

        if answer == 3:
            print(f'Текущий город: {name_city}')
            new_city.append(input('Новый город:'))
        else:
print('\n'.join(city))
answer = int(input('Выберите действие: '))

            if answer == 4:
                new_city.remove(input('Введите название города:'))
                print(f' Город удален!')
            else:
print('\n'.join(city))
answer = int(input('Выберите действие: '))

                if answer == 5:
                    print('Программа завершает работу.')
                else:
