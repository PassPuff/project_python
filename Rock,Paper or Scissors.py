import random

print('Игра камень, ножницы, бумага!')
choose = int(input('Что ты выберешь? 0 - Камень, 1 - Бумага, 2- ножницы!?:'))

tools = ['🪨', '📜', '✂️']
random_num = random.randint(0, 2)
choose_computer = tools[random_num]
print(tools[choose])


if choose == 0 and random_num == 2:
    print(choose_computer)
    print('Вы выиграли!\nКАМЕНЬ ПОБЕЖДАЕТ НОЖНИЦЫ')
elif choose == 0 and random_num == 1:
    print(choose_computer)
    print('Вы проиграли!\nБУМАГА ПОБЕЖДАЕТ КАМЕНЬ')
elif choose == 0 and random_num == 0:
    print(choose_computer)
    print('НИЧЬЯ')


if choose == 1 and random_num == 2:
    print(choose_computer)
    print('Вы проиграли!\nНОЖНИЦЫ ПОБЕЖДАЮТ БУМАГУ')
elif choose == 1 and random_num == 0:
    print(choose_computer)
    print('Вы проиграли!\nКАМЕНЬ ПОБЕЖДАЕТ НОЖНИЦЫ')
elif choose == 1 and random_num == 1:
    print(choose_computer)
    print('НИЧЬЯ')


if choose == 2 and random_num == 1:
    print(choose_computer)
    print('Вы выиграли!\nНОЖНИЦЫ ПОБЕЖДАЮТ БУМАГУ')
elif choose == 2 and random_num == 0:
    print(choose_computer)
    print('Вы проиграли!\nКАМЕНЬ ПОБЕЖДАЕТ НОЖНИЦЫ')
elif choose == 2 and random_num == 2:
    print(choose_computer)
    print('НИЧЬЯ')
