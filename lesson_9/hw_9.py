"""
Написати програму, для ведення та перегляду нотаток. Нажаль, поки ми не працюємо з файлами,
тому нотатки видаляються після завершення роботи програми.
Програма пропонує користувачу вводити ключові слова, та опрацьовує їх. Перелік ключових слів:
add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
earliest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшоїдо найдовшої
Якщо довжина нотаток однакова, то їх порядок відображення не принциповий.
"""
from datetime import datetime


def add(notes: dict):
    now = datetime.now()
    notes[now] = input('Введіть нотатку: ')


def earliest(notes: dict):
    """
    Розраховує нотатки у хронологічному порядку - від найранішої до найпізнішої
    :param notes: словник, де ключ - час введення, значення - нотатки
    :return: latest - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
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
    :return: latest - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
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
    :return: longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
    """
    print('від найдовшої до найкоротшої:')
    values = sorted(notes.values(), key=len, reverse=True)
    for value in values:
        print(value)


def shortest(notes: dict):
    """
    Розраховує нотатки у порядку їх довжини - від найкоротшоїдо найдовшої
    :param notes: словник, де ключ - час введення, значення - нотатки
    :return: shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшоїдо найдовшої
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
    :return: виконання відповідальну функцію
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
    while comand_ != 'exit':
        comand_ = input_comand()
        exec_comand(comand_, notes_)
