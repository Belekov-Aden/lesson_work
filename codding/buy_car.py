
car = input('Какую машину  в хотите? ')
car_year = int(input('Какого года? '))
mileage_car = int(input('Пробег машины: '))
color_car = input('Какого цвета: ')
car_helm = input('Расположение руля: ')
host_car = int(input('Сколько хозяинев: '))
cost_car = int(input('Стоимость машины: '))

if car == 'тойота' or car == 'лексус':
    print(f'{car}')
if  car_year > 2004:
    print(f'{car_year}')
if mileage_car ==  150000:
    print(f'{mileage_car}')
if color_car == 'white' or cost_car == 'grey':
    print(f'{cost_car}')
if car_helm == 'left' or car_helm == 'right':
    print(car_helm)
if host_car <= 2:
    print(host_car)
if cost_car < 10000:
    print(cost_car)
else:
    print(f'{car}\n{car_year}')
    if mileage_car > 200000 and cost_car < 8000:
        print(f'{mileage_car}\n {cost_car}')
