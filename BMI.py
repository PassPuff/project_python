height = float(input('Введите ваш рост в метрах: '))
weight = float(input('Введите ваш вес в килограммах: '))
bmi = round(weight / height ** 2, 1)

if bmi < 18.5:
    print(f'Вы имеете недостаточный вес,индекс массы тела =  {bmi}')
elif bmi < 25:
    print(f'Вы имеете нормальный вес, индекс массы тела =  {bmi}')
elif bmi < 30:
    print(f'Вы имеете лишний вес, индекс массы тела =  {bmi}')
elif bmi < 35:
    print(f'Вы толстый, индекс массы тела =  {bmi}')
else:
    print(f'Вы клинически тучный,индекс массы тела =  {bmi}')
