print('Добро пожаловать на аттракционы')
height = int(input('Введите ваш рост в сантиметрах: '))
age = int(input('Введите ваш возраст: '))
total = 0

if height >= 120:
    if age < 12:
        total = 300
        print(f'Тариф детский: стоимость билета {total} рублей')
    elif age <= 18:
        total = 500
        print(f"Тариф подросток: стоимость билета {total} рублей")
    elif age >= 45 or age <= 55:
        total = 0
        print(f"Вам повезло быть сегодня тут: стоимость билета {total} рублей")
    else:
        total = 800
        print(f'Тариф взрослый: стоимость билета {total} рублей')

    photo = (input('Вам напечатать ваше фото с аттракциона?( да / нет)'))
    if photo == 'да':
        total += 150
        print(f'Итого с вас за фото и билет {total} рублей')
    else:
        print(f'Итого за билет {total} рублей')


else:
    print('Прошу прощения,но мы не можем вас пропустить \n =/')