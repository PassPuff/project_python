from art import logo
from alhabet import alphabet

print(logo)


def ceasar(text_, shift_, direction_):
    new_message = ''
    for i in text_:
        if i in alphabet:
            index = alphabet.index(i)
            if direction_ == 'decode':
                shift_ *= -1
            new_position = index + shift_
            new_message += alphabet[new_position]
        else:
            new_message += i

    print(f'The {direction_}d text is" {new_message}"')


again = False

while not again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 25

    ceasar(text, shift, direction)
    run = input('Run again? y|n ')
    if run == 'n':
        again = True
