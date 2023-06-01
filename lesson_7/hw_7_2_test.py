"""
II. Програма перевіряє чи існує трикутник по введеним сторонам та відображає його периметр та площу якщо він існує.
Потрібно реалізувати чотири функції:
Зчитування сторони трикутника (саме додатнього числа, а не того що може ввести користувач) та повернення цього значення
Перевірка можливості існування трикутника та поверненням True/False
Підрахунок периметру трикутника
Підрахунок площі трикутника

Усі функції мають приймати параметри, не використовувати нічого з зовнішньої області видимості та користуватись return,
Головна частина відповідає за діалог з користувачем та основну логіку
(виклик усіх функцій у вірному порядку та вивід відповіді).

Математична частина
Трикутник існує тоді, коли сумма двох його сторін більше за третю сторону.
Тобто у трикутника зі сторонами a, b, c мають виконуватись такі вимоги: a + b > c. a + c > b, b + c > a.
Периметр трикутника - то є сума всіх його сторін, тобто p = a + b + c
Площа трикутника за сторонами знаходиться через напівпериметр та корінь квадратний sqrt (можна імпортувати з math):
half_p = p / 2
s = sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c)
"""

from math import sqrt


# Зчитування сторони трикутника (саме додатнього числа, а не того що може ввести користувач)
# та повернення цього значення
def triangle_input():
    """
    Отвечает за считывание у пользователя строки и конвертации её в число
    Считывание до тех пор, пока введённая строка не удовлетворит все условия
    :return: считанное у пользователя число (положительное) - сторона треугольника
    """
    while True:
        side = input('Введіть сторону трикутника: ')  # ввод строку
        try:
            side = float(side)  # преобразовать в строку
            if side <= 0:  # если число отрицательное, напечатать ошибку, ввести заново
                print('Введіть сторону трикутника - саме додатне число')
            else:
                return side
        except Exception:  # если ввод не числа, напечатать ошибку, ввести заново
            print('Некоректний ввід. Введіть сторону трикутника - число: ')


# Перевірка можливості існування трикутника та поверненням True/False
def triangle_test(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
        return True
    else:
        return False


# Підрахунок периметру трикутника
def triangle_perimeter(side1, side2, side3):
    # if triangle_test(side1, side2, side3) == True:
    perimeter = side1 + side2 + side3
    return perimeter


# Підрахунок площі трикутника
def triangle_area(side1, side2, side3):
    # if triangle_test(side1, side2, side3) == True:
    half_p = triangle_perimeter(side1, side2, side3) / 2
    square = sqrt(half_p * (half_p - side1) * (half_p - side2) * (half_p - side3))
    return square
    # else:
    #      return print('Площа трикутника не існує')


# Приклад використання функцій
side1_exepl = triangle_input()
side2_exepl = triangle_input()
side3_exepl = triangle_input()


triangle_test_exepl = triangle_test(side1_exepl, side2_exepl, side3_exepl)
if triangle_test_exepl:
    print("Існує трикутник")
    triangle_perimeter_exepl = triangle_perimeter(side1_exepl, side2_exepl, side3_exepl)
    print("Периметр трикутника:", triangle_perimeter_exepl)

    triangle_square_exepl = triangle_area(side1_exepl, side2_exepl, side3_exepl)
    print("Площа трикутника:", triangle_square_exepl)
else:
    print("Трикутник не існує")


# triangle_test_exepl = triangle_test(side1_exepl, side2_exepl, side3_exepl)
# print("Існує трикутник?", triangle_test_exepl)
#
# triangle_perimeter_exepl = triangle_perimeter(side1_exepl, side2_exepl, side3_exepl)
# print("Периметр трикутника:", triangle_perimeter_exepl)
#
# triangle_square_exepl = triangle_area(side1_exepl, side2_exepl, side3_exepl)
# print("Площа трикутника:", triangle_square_exepl)
