
#input user
language = input('Какой язык прог-ия знаете?[python/java/javascripts] ')
age = int(input('Возраст: '))
skils = int(input('Опыт работы: '))
salary = int(input('Желаемая запралта: '))

#if-elif-else
if language == 'java' or language == 'python' or language == 'javascript':
    print(f'Язык программирования: {language}')
else:
    print('Кандидат не подходит!')
    if age > 18 and age <= 65:
        print(f'Возраст {age}')
    else:
        print('Кандидат не подходит!')
        if skils > 3:
            print(f'Опыт работы {skils}')
        else:
            print('Кандидат не подходит!')
            if salary < 60000:
                print(f'Желаемая зарпалата {salary}')
                print(f'Кандидат подходит!')
            else:
                print('Кандидат не подходит!')