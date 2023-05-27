"""
I. Написати програму що перевіряє чи є введена строка дзеркальною (паліндромом).
Наприклад, слово "довод", фраза "Аби ріці риба" або числа 84348 та 45677654 - дзеркальні.
Вхідну строку треба перевести в один регістр, позбавити пробілів, табуляцій,
переносів на нову строку та розділових знаків.
Вхідні дані:
строка
На виході
Відповідь чи є строка паліндромом
"""
import string

while True:
    words = input("Введіть звернення: ").lower()
    words = words.strip()
    if words != '':
        try:
            words = words.split()  # разбиение по словам
            new_words = list()
            for word in words:
                word = word.strip(string.punctuation)  # убрать пунктуации для каждого слова
                if not word:  # если слово пустое
                    continue  # прервать текущую итерацию и перейти к следующей
                new_words.append(word)  # добавить слова без пунктуаций в новій словарь
            new_words_without_punctuation = ''.join(new_words)  # объеденить слова в одно слово
            # new_words_without_punctuation_2 = new_words_without_punctuation[::-1]
            if new_words_without_punctuation == new_words_without_punctuation[::-1]:  # сравнения слова и зеркальное
                print(f'Строка {new_words_without_punctuation} є паліндромом')
            else:
                print('Строка не є паліндромом')
            break
        except Exception:
            print('Строка не повинна бути пустою')
    else:
        print('Строка не повинна бути пустою')

# print(words)
# print(new_words)
# print(new_words_without_punctuation)
# print(type(new_words_without_punctuation))
# print(new_words_without_punctuation_2)
