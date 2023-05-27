"""
Написати програму, що зчитує числа від користувача поки не буде введено ключове слово sum.
Коли воно введено, програма повідомляє сумму введених чисел та завершує виконання.
Якщо користувач вводить не число і не ключове слово sum, програма повідомляє про некоректне введення,
але продовжує виконання і пам'ятає контекст.
Наприклад:
Ваше число: 1
Ваше число: 6.5
Ваше число: 9
Ваше число: -17
Ваше число: Число
Введіть число або sum будь-ласка!
Ваше число: 3.5
Ваще число: sum
3
"""

list_numbers = list()
input_sum = False
while not input_sum:
    input_number = input("Ваше число: ")
    find_number = False
    #  якщо введено слово sum, то розраховує сумму введених чисел та завершує виконання
    if input_number.lower() == 'sum':
        print(sum(list_numbers))
        find_number = True
        input_sum = True  # завершити програму
    #  якщо введено слово не sum,
    #  якщо введено число то додати до списку
    #  якщо введено не число то видає ошибку, продовжує виконання
    if input_number.lower() != 'sum':
        try:
            input_number = float(input_number)
            list_numbers.append(input_number)
            find_number = True
        except Exception:
            print('Введіть число або sum будь-ласка!')
    # print(list_numbers)