"""
#Секунди у дні/години/хвилини
# Написати функцію.
# ВхідніПараметри:
# ціле число
# Повертає: словник з ключами days, hours, minutes, seconds та їх відповідними значеннями
# Наприклад:
# function(60 * 60 + 30) -> {"days": 0, "hours": 1, "minutes": 0, "seconds": 30}
# function(60 * 60 * 25) -> {"days": 1, "hours": 1, "minutes": 0, "seconds": 0}
# function(60 * 20 + 15) -> {"days": 0, "hours": 0, "minutes": 20, "seconds": 15}
# Підказка: метод divmod та таблиця конвертацій
# 1 день = 24 години
# 1 година = 60 хвилин
# 1 хвилина = 60 секунд
"""


def number_input():
    """
    ВВод корректности числа в соответствии условий
    :return: считанное у пользователя число (положительное)
    """
    while True:
        number_inp = input('Введіть число: ')  # ввод строку
        try:
            number_inp = int(number_inp)  # преобразовать в строку
            if number_inp <= 0:  # если число отрицательное, напечатать ошибку, ввести заново
                print('Введіть число: - саме додатне число')
            else:
                return number_inp
        except Exception:  # если ввод не числа, напечатать ошибку, ввести заново
            print('Некоректний ввід.')


# def time_from_second(second: int):
#     """
#     Функція яка перетворює Секунди у дні/години/хвилини
#     :param second: секунды
#     :return: словник з ключами days, hours, minutes, seconds та їх відповідними значеннями
#     """
#     days_time = second // (60 * 60 * 24)
#     hours_time = (second % (60 * 60 * 24)) // (60 * 60)
#     minutes_time = (second % (60 * 60 * 24)) % (60 * 60) // 60
#     seconds_time = (second % (60 * 60 * 24)) % (60 * 60) % 60
#     return {"days_time": days_time, "hours_time": hours_time,
#     "minutes_time": minutes_time, "seconds_time": seconds_time}


def time_from_second(second: int):
    """
    Функція яка перетворює Секунди у дні/години/хвилини
    :param second: секунды
    :return: словник з ключами days, hours, minutes, seconds та їх відповідними значеннями
    """
    # days_time = second // (60 * 60 * 24)
    days_time = divmod(second, 86400)[0]
    hours_time = divmod(second, 86400)[1] // (60 * 60)
    minutes_time = divmod(second, 86400)[1] % (60 * 60) // 60
    seconds_time = divmod(second, 86400)[1] % (60 * 60) % 60
    return {"days_time": days_time, "hours_time": hours_time,
            "minutes_time": minutes_time, "seconds_time": seconds_time}


if __name__ == '__main__':
    datatime = number_input()
    print(time_from_second(datatime))
