"""
II. Програма перевіряє чи існує трикутник по введеним сторонам та відображає його периметр та площу якщо він існує.
Потрібно реалізувати чотири функції:
Зчитування сторони трикутника (саме додатнього числа, а не того що може ввести користувач) та повернення цього значення
Перевірка можливості існування трикутника та поверненням True/False
Підрахунок периметру трикутника
Підрахунок площі трикутника

Усі функції мають приймати параметри, не використовувати нічого з зовнішньої області видимості та користуватись return,
Головна частина відповідає за діалог з користувачем та основну логіку (виклик усіх функцій у вірному порядку та вивід відповіді).

Математична частина
Трикутник існує тоді, коли сумма двох його сторін більше за третю сторону.
Тобто у трикутника зі сторонами a, b, c мають виконуватись такі вимоги: a + b > c. a + c > b, b + c > a.
Периметр трикутника - то є сума всіх його сторін, тобто p = a + b + c
Площа трикутника за сторонами знаходиться через напівпериметр та корінь квадратний sqrt (можна імпортувати з math модулю):

half_p = p / 2
s = sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))
"""
# Зчитування сторони трикутника (саме додатнього числа, а не того що може ввести користувач) та повернення цього значення
def triangle():
    slice_list = list()
    while len(slice_list) < 3:
        side = input('Введіть сторону трикутника: ')
        try:
            side = float(side)
            if side <= 0:
                print('Введіть сторону трикутника: - саме додатне число')
            else:
                slice_list.append(side)
        except Exception:
            print('Введіть сторону трикутника: - число: ')
    return slice_list

h = triangle()
print(h)

# Перевірка можливості існування трикутника та поверненням True/False
def triangle_test():
    sides = triangle()
    print(sides)

    # if sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]:
    #     result = True
    # else:
    #     result = False
    # return result

a = triangle_test()
print(a)

# Підрахунок периметру трикутника
# def triangle_perimeter(slice_list):
#     slice_list = triangle_test()
#     return slice_list
    # if res == True:
    #     # sides = triangle([])
    #     print(slice_list)
    #     return slice_list
    # else:
    #     perimeter = False
    #     return perimeter


# m = triangle_perimeter(triangle([]))
# print(m)

