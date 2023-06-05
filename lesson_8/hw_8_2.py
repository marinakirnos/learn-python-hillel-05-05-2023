"""
Просте число до 100
https://uk.wikipedia.org/wiki/Просте_число
Написати функцію
Вхідні параметри:
ціле число (до 100)
Повертає: флаг (bool) чи є число простим
Наприклад:
function(5) -> True
function(8) -> False
function(37) -> True
Підказка: мати перелік простих чисел (до 100) і перевіряти на наявність: x in simple_set
(бажано використати set() {2, 3, 5, 7...})
"""


def number_input():
    """
    ВВод корректности числа в соответствии условий
    :return: считанное у пользователя число (положительное)
    """
    while True:
        number_inp = input('Введіть число від 1 до 100: ')  # ввод строку
        try:
            number_inp = int(number_inp)
            if 1 <= number_inp <= 100:
                return number_inp
            else:
                print('Некоректний ввід. число від 1 до 100')
        except Exception:  # если ввод не числа, напечатать ошибку, ввести заново
            print('Некоректний ввід.')


# Variant 1
def is_prime_number(number: int):
    simple_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
    if number in simple_set:
        return True
    else:
        return False


# Variant 2
# def is_prime_number(number: int):
#     """
#     Перевірка числа чи є воно прости
#     :param number: число от 1 до 100
#     :return: перевыряє чи є число простим True/False
#     """
#     if number > 1:  # Число меньше 2 не может быть простым
#         for i in range(2, number):
#             if number % i == 0:  # Число делится нацело на i, значит, оно не является простым
#                 return False
#         return True
#     return False


if __name__ == '__main__':
    prime_number = number_input()
    print(is_prime_number(prime_number))
