# var 3
# заготовки ключових фраз
words_welcome = ('привіт', 'хай', 'доброго дня', 'доброго вечора')
words_make = ('як справи', 'що робиш', 'чим займаєшся')
words_film = ('фільм', 'кінотеатр', 'серіал')
words_bay = ('бувай', 'надобраніч', 'гудбай', 'до зустріч')
input_bay = False
counter = 0  # для удобства нумерации вопросов
while not input_bay:
    input_string = input(f"Введіть звернення {counter + 1}: ").lower()
    find_word = False
    # перебор ключевых фраз в заготовки words_welcome
    # если ключевая фраза найдена в input_str, то вывести ответ
    for word in words_welcome:
        if word in input_string:
            print('Доброго вечора, я бот з України!')
            find_word = True
    # перебор ключевых фраз в заготовки words_make
    # если ключевая фраза найдена в input_str, то вывести ответ
    for word in words_make:
        if word in input_string:
            print('Вчусь програмувати на Python!')
            find_word = True
    # перебор ключевых фраз в заготовки words_film
    for word in words_film:
        if word in input_string:
            print('Соррі що втручаюсь, не знаю про що йдеться мова, але подивіться серіал/фільм - '
                  'Друзі, він просто бомба!')
            find_word = True
    # перебор ключевых фраз в заготовки words_bay
    for word in words_bay:
        if word in input_string:
            print("Побачимось у мережі, I'll be back")
            find_word = True
            input_bay = True # завершити програму
    # если в введеном выражении нет ключевых слов вывести сообщение
    if not find_word:
        print('Дуже цікаво, але, нажаль, нічого не зрозуміло :( ')
    counter += 1
