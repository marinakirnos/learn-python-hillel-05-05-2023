"""
# var 1
import string
words_welcome = ('привіт', 'хай', 'доброго дня', 'доброго вечора')
words_make = ('як справи', 'що робиш', 'чим займаєшся')
words_film = ('фільм', 'кінотеатр', 'серіал')
words_bay = ('бувай', 'надобраніч', 'гудбай', 'до зустріч')
input_bay = False
counter = 0
while not input_bay:
    words = input(f"Введіть звернення {counter + 1}: ").lower()
    words = words.split(' ')
    new_words = list()
    for word in words:
        new_words.append(word.strip(string.punctuation))
    # print(new_words)
    # print(words)
    find_word = False
    for word in new_words:
        if word in words_welcome:
            print('Доброго вечора, я бот з України!')
            find_word = True
        elif word in words_make:
            print('Вчусь програмувати на Python!')
            find_word = True
        elif word in words_film:
            print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал/фільм - Друзі, він просто бомба!')
            find_word = True
        elif word in words_bay:
            print("Побачимось у мережі, I'll be back")
            find_word = True
            input_bay = True
    if not find_word:
        print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')
    counter += 1
    print(counter)
"""
"""
# var 2
import string
words_welcome = ('привіт', 'хай', 'доброго дня', 'доброго вечора')
words_make = ('як справи', 'що робиш', 'чим займаєшся')
words_film = ('фільм', 'кінотеатр', 'серіал')
words_bay = ('бувай', 'надобраніч', 'гудбай', 'до зустріч')
input_bay = False
counter = 0
while not input_bay:
    words = input(f"Введіть звернення {counter + 1}: ").lower()
    words = words.split(' ')
    new_words = list()
    for word in words:
        new_words.append(word.strip(string.punctuation))
    # print(new_words)
    # print(words)
    if set(new_words).intersection(words_welcome) != set():
        print('Доброго вечора, я бот з України!')
        find_word = True
    elif set(new_words).intersection(words_make) != set():
        print('Вчусь програмувати на Python!')
        find_word = True
    elif set(new_words).intersection(words_film) != set():
        print('Соррі що втручаюсь, не знаю про що йдеться мова, але подивіться серіал/фільм - Друзі, він просто бомба!')
        find_word = True
    elif set(new_words).intersection(words_bay) != set():
        print("Побачимось у мережі, I'll be back")
        find_word = True
        input_bay = True
    else:
        print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')
    counter += 1
    print(counter)
"""

# var 4
secret_word_1 = ('привіт', 'хай', 'доброго дня', 'доброго вечора')
secret_word_2 = ('як справи', 'що робиш', 'чим займаєшся')
secret_word_3 = ('фільм', 'кінотеатр', 'серіал')
secret_word_4 = ('бувай', 'надобраніч', 'гудбай', 'до зустріч')
counter = 0
input_bay = False
while not input_bay:
    input_string = input("Введіть звернення: ").lower()
    # counter = counter + 1
    find_word = False
    for word in secret_word_1:
        if word in input_string:
            print('Доброго вечора, я бот з України!')
            find_word = True
    for word in secret_word_2:
        if word in input_string:
            print('Вчусь програмувати на Python!')
            find_word = True
    for word in secret_word_3:
        if word in input_string:
            print('Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал/фільм - Друзі, він просто бомба!')
            find_word = True
    for word in secret_word_4:
        if word in input_string:
            print("Побачимось у мережі, I'll be back")
            find_word = True
            input_bay = True
    if not find_word:
        print('Дуже цікаво, але, нажаль, нічого не зрозуміло :(')


