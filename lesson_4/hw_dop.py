# task 1
import math
number_1 = ''
while type(number_1) != float:
    number_1 = (input('Введите число первое: '))
    try:
        # print('Это происходит до отлова ошибки')
        number_1 = float(number_1)
        # print('Это происходит после отлова ошибки')
    # обработка ошибки
    # срабатывает только если в блоке try была ошибка
    except Exception:
        print(f'Не удалось получить число из ввода: "{number_1}", повторите пожалуйста попытку')

number_2 = ''
while type(number_2) != float:
    number_2 = (input('Введите число второе: '))
    try:
        number_2 = float(number_2)
    except Exception:
        print(f'Не удалось получить число из ввода: "{number_2}", повторите пожалуйста попытку')
if number_1 > number_2:
    df = number_1 - number_2
    print(f' {number_1} больше {number_2} на {df}')
    if number_2 != 0:
        del_ = round(abs(number_1 / number_2), 2)
        print(f' {number_1} больше {number_2} в {del_} раза')
    else:
        print(f' {number_2} = 0, делить на 0 нельзя!')
if number_1 == number_2:
    df = number_1 - number_2
    print(f' {number_1} = {number_1}')
    if number_2 != 0:
        del_ = round(abs(number_1 / number_2), 2)
        print(f' {number_1} больше {number_2} в {del_} раза')
    else:
        print(f' {number_2} = 0, делить на 0 нельзя!')
if number_1 < number_2:
    df = number_2 - number_1
    print(f' {number_2} больше {number_1} на {df}')
    if number_1 != 0:
        del_ = round(ab(number_2 / number_1), 2)
        print(f' {number_2} больше {number_1} в {del_} раза')
    else:
        print(f' {number_1} = 0, делить на 0 нельзя!')

"""
# Програма приймає два числа та повідомляє яке з них менше та у скільки разів (20 менше 100 у 5 разів).
# Зверніть увагу на форматування строки відповіді, найчастіше float числа як число Пі=3.14159...
# відображають лише з 1-2 цифрами після крапки
"""