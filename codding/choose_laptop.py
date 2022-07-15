print('Хотите выбрать ноутбук!')
ram = int(input('Сколько гб ОЗУ: '))
disk = int(input('Сколько гб жесткого диска: '))
disk_form = input('А какой имеено SSD / HDD ')
cost_laptop = int(input('А какой бюджет для покупики? '))
status_laptop = input('новый / бу' )

if ram == 4 and ram <= 8 and disk >= 256 and disk_form == 'SSD' or  disk_form == 'HDD' and disk >= 1000 and cost_laptop < 1000 and status_laptop == 'новый':
    print('Вам подходит этот ноутбук!!!!')
else:
    print('Вам не подходит!')

