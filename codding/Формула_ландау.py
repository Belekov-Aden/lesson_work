#Формула KMT / (N2P)
print('Узнаем ваше женскую привлекательность ))')
chest = int(input('Введите обьем груди: '))    #K
hips = int(input('Введие обьем бёдер: '))      #M
waist = int(input('Введите обьем талий: '))     #N
growth = int(input('Введите рост:')) #T
wt = int(input('Введите вес: '))  #P

l_1 = chest*hips*growth
l_2 = waist**2*wt
woman = l_1/l_2
print('Ваша привлекательность: ', int(woman))

print('Если >= 5 вы привлекательны\n'
      'а если =< 2,вам нужно идти в зал')
