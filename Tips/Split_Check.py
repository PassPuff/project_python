print('Добро пожаловать в калькулятор чаевых!)')
total_sum_check = input('Введите общую сумму чека в рублях ? ₽ ')
tip_amount = input('Какой процент от чека оставите чаевыми 10% ,12% или 15%? ')
persons = input('На сколько персон поделить счет? ')

total_sum = (float(total_sum_check) * int(tip_amount) / 100) + float(total_sum_check)
split_check = total_sum / int(persons)

print(f'Итого с {persons} человек по {round(split_check ,2)} ₽ ')
