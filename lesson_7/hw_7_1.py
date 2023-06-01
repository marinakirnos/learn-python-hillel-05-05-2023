import string
def read_user_number(user_prompt, lower_bound=2):
    while True:
        words = input(f'{user_prompt}').lower()
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
                if len(new_words_without_punctuation) > 1:
                    if new_words_without_punctuation == new_words_without_punctuation[::-1]:  # сравнения слова и зеркальное
                        return print(f'Строка {new_words_without_punctuation} є паліндромом')
                    else:
                        return print('Строка не є паліндромом')
                else:
                    print('Строка повинна мати от 2 символів')
            except Exception:
                print('Строка не повинна бути пустою та повина мати от 2 символів')
        else:
            print('Строка не повинна бути пустою')

a = read_user_number('Введіть звернення:')

# print(a)