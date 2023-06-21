"""
Написати програму, для ведення та перегляду нотаток. викорисовувати службового файлу, в який записуються нотатки.
Ім'я файлу задається програмою автоматично.
Програма пропонує користувачу вводити ключові слова, та опрацьовує їх. Перелік ключових слів:
add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
earliest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшоїдо найдовшої
Якщо довжина нотаток однакова, то їх порядок відображення не принциповий.
Використати програму про ведення нотаток з попереднього ДЗ та доповнити її функціонал використанням службового файлу,
в який записуються нотатки для продовження роботи.
Ім'я файлу задається програмою автоматично.
Очікувана нова поведінка програми:
Якщо її не було раніше, треба додати команду exit та назвати її save & exit
Під час виконання команди save & exit перед виходом програма зберігає всі поточні нотатки у текстовий файл
Коли програма починає своє виконання, з файлу (за наявності) завантажуються у поточну пам'ять всі нотатки та
коректно взаємодіють з присутнім функціоналом програми (всі 4 види відображень)
"""
from datetime import datetime


def add(notes: dict):
    now = str(datetime.now())
    notes[now] = input('Введіть нотатку: ')

    out = open('data.txt', mode='a', encoding='utf-8')
    for key in notes:
        out.write(key + '\n')
        out.write(notes[key] + '\n')
    print("Нотатка додана успішно.")


def input_notes():
    input_notes_new = {}
    input = open('data.txt')
    key = input.readline().strip()
    note = input.readline().strip()
    while key:
        input_notes_new[key] = note
        key = input.readline().strip()
        note = input.readline().strip()
    return input_notes_new


def earliest(notes: dict):
    """
    Розраховує нотатки у хронологічному порядку - від найранішої до найпізнішої
    :param notes: словник, де ключ - час введення, значення - нотатки
    """
    print('Від найранішої до найпізнішої:')
    key_sort_list = sorted(list(notes.keys()))  # var 1
    # key_sort_list = dict(sorted(notes.items(), key=lambda element: element[0]))  # var 2
    for key in key_sort_list:
        # print(key, notes[key])
        print(notes[key])


def latest(notes: dict):
    """
    Розраховує нотатки у хронологічному порядку - від найпізнішої до найранішої
    :param notes: словник, де ключ - час введення, значення - нотатки
    """
    print('Від найпізнішої до найранішої:')
    key_sort_list = sorted(list(notes.keys()), reverse=True)  # var 1
    # key_sort_list = dict(sorted(notes.items(), key=lambda element: element[0], reverse=True))  # var 2
    for key in key_sort_list:
        print(notes[key])


def longest(notes: dict):
    """
    Розраховує нотатки у порядку їх довжини - від найдовшої до найкоротшої
    :param notes: словник, де ключ - час введення, значення - нотатки
    """
    print('від найдовшої до найкоротшої:')
    values = sorted(notes.values(), key=len, reverse=True)
    for value in values:
        print(value)


def shortest(notes: dict):
    """
    Розраховує нотатки у порядку їх довжини - від найкоротшоїдо найдовшої
    :param notes: словник, де ключ - час введення, значення - нотатки
    """
    print('від найкоротшоїдо найдовшої:')
    values = sorted(notes.values(), key=len)
    for value in values:
        print(value)


def input_comand() -> str:
    """
    Ввод команди - ключові слова: add, earliest, latest, longest, shortest
    :return: командa
    """
    comand = input('> ')
    return comand


def exec_comand(comand: str, notes: dict):
    """
    В залежності від введеної команди виконую відповідальну функцію
    :param comand: команда
    :param notes: нотатки
    """
    if comand == 'add':
        add(notes)
    elif comand == 'earliest':
        earliest(notes)
    elif comand == 'latest':
        latest(notes)
    elif comand == 'longest':
        longest(notes)
    elif comand == 'shortest':
        shortest(notes)
    elif comand != 'exit':
        print('Не коректне введення. Виберіть: add, earliest, latest, longest, shortest')


if __name__ == '__main__':
    comand_ = ''
    notes_ = {}
    f = open('data.txt', mode='r', encoding='utf-8')

    while comand_ != 'exit':
        comand_ = input_comand()
        exec_comand(comand_, notes_)
    print(input_notes())