#ЗП = (О/Дк * Дф + П) * ((100 - Н) / 100) — У

salary_oclad = int(input('Введите заработную плата по окладу:' ))
rabotnik = int(input('оклад работника:' ))
dk = int(input('количество календарных дней по производственному календарю: '))
df = int(input('количество фактически отработанных дней: '))
p = int(input('премии в сумме: '))
h = int(input('Налог на доход физического лица, который составляет 13%: '))
y = int(input('штрафы и.д: '))

zp = (rabotnik / dk * df + p) * ((100 - h) / 100) - y
print(int(zp))