import random
from words_game import word_list
from art_game import stages, logo

print(logo)
random_word = random.choice(word_list)
word_len = len(random_word)
lives = 6
hide_world = []

for _ in range(word_len):
    hide_world += '_'
print(hide_world)

end_game = False

while not end_game:
    guess_letter = input('Угадайте букву ?').lower()

    for position in range(word_len):
        letter = random_word[position]
        if letter == guess_letter:
            hide_world[position] = letter

    if guess_letter not in hide_world:
        lives -= 1
        print(f'у вас осталось {lives} жизней \n {stages[lives]}')
        if lives == 0:
            end_game = True
            print('Yoy lose!')
    print(hide_world)

    if '_' not in hide_world:
        end_game = True
        print('Yoy win')
