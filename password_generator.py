import random

letters = ['a', 'b' 'c', 'd', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', ' q', 'r', 's', 'u', 'w', 'x', 'y', '2', 'A',
           'I', 'B', 'C', 'D', 'E', 'F', 'G', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', '§', 'T', 'H', 'I', 'J', 'K', 'U', 'V',
           'W', 'X', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#' '%', '&', '(', ')', '*', '+']
print("Добро пожаловать в генератор пароля!")

length_pass = int(input('Какой длины хотите создать пароль? \n'))
symbol = int(input('Сколько символов? \n'))
number = int(input('Сколько цифр должно быть в пароле ? \n'))

password = ''

if len(password) <= length_pass:
    for sym in range(symbol):
        password += random.choice(symbols)

    for num in range(number):
        password += random.choice(numbers)

    for item in range(length_pass - symbol - number):
        password += random.choice(letters)

new_password = list(password)
random.shuffle(new_password)
result = ''.join(new_password)

print(result)




