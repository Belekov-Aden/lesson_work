#Определить четверть координатной плоскости

x = int(input('Координата x:'))
y = int(input('Кооринат y:'))

if x > 0 and y > 0:
    print('1 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0 and y < 0:
    print('4 четверть')