
area = input('Введите район: ')
cost_home = int(input('Стоимость дома '))
materials_home = input('Материал создание дома: ')
size_home = int(input('Какой нужен участок: '))

if area == 'чон арык' and materials_home == 'кирпич' and size_home >=4 and cost_home <= 50000:
    print(f'Дом из кирпича в районе {area}  участок {size_home} соток и стоимость составляет {cost_home}')
elif materials_home == 'пескоблок' and size_home >= 5 and cost_home <= 45000:
    print(f'Дом из пескоблока,в районе {area},{size_home} соток, и стоимость состовялет {cost_home}')
else:
    if area == 'орто сай' and  materials_home == 'кирпич' and size_home >=4 and cost_home <= 50000:
        print(f'Дом из кирпича в районе {area}  участок {size_home} соток и стоимость составляет {cost_home}')
    elif materials_home == 'пескоблок' and size_home >= 5 and cost_home <= 45000:
        print(f'Дом из пескоблока,в районе {area},{size_home} соток, и стоимость состовялет {cost_home}')
    else:
        print(f'К сожалению вам не подходит!')