"""
I. Програма повторює будь яку вашу вправу з "ДЗ 1. Вправи за типами даних int та float" або
"ДЗ 5.Вправи на slice за типом даних str".
Aле ж тепер потрібно розділити виконання програми на головну частину та функцію def.
В функцію def потрібно передати вхідні дані, сама функція містить в собі логіку вирішення завдання.
Функція має повернути (return) відповідь у головну частину.
Головна частина відповідає за діалог з користувачем, отримання вхідних даних
(дозволяється та заохочується використання додаткових функцій),
викликання функції вирішення задачі та обробка отриманої відповіді (виведення її на екран).
"""
import string

while True:
    words = input('Введіть звернення: ').lower()
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
            break
        except Exception:
            print('Строка не повинна бути пустою та повина мати от 2 символів')
    else:
        print('Строка не повинна бути пустою')


def palindrome(palindrome_word):
    """
    Сравнения введенного слова пользователем и его зеркальное
    :param palindrome_word:
    :return: результат является ли слово паліндромом - True/False
    """
    if palindrome_word == palindrome_word[::-1]:
        return True
    else:
        return False


word_1_exemp = palindrome(new_words_without_punctuation)
if word_1_exemp:
    print(f'{new_words_without_punctuation} є паліндромом')
else:
    print(f'{new_words_without_punctuation} не є паліндромом')
