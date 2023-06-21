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


def load_notes():
    try:
        input_notes = {}
        input_file = open('data.txt', 'r', encoding='utf-8')
        key = input_file.readline().strip()
        note = input_file.readline().strip()
        while key:
            input_notes[key] = note
            key = input_file.readline().strip()
            note = input_file.readline().strip()
        input_file.close()
        return input_notes
    except FileNotFoundError:
        return {}


def save_notes(notes: dict):
    output_file = open('data.txt', 'a', encoding='utf-8')
    for key in notes:
        output_file.write(key + '\n')
        output_file.write(notes[key] + '\n')
    output_file.close()
    print("Нотатки збережено успішно.")


def earliest(notes: dict):
    """
    Розраховує нотатки у хронологічному порядку - від найранішої до найпізнішої
    :param notes: словник, де ключ - час введення, значення - нотатки
    """
    print('Від найранішої до найпізнішої:')
    key_sort_list = sorted(list(notes.keys()))  # var 1
    for key in key_sort_list:
        print(notes[key])


def latest(notes: dict):
    """
    Розраховує нотатки у хронологічному порядку - від найпізнішої до найранішої
    :param notes: словник, де ключ - час введення, значення - нотатки
    """
    print('Від найпізнішої до найранішої:')
    key_sort_list = sorted(list(notes.keys()), reverse=True)  # var 1
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
    elif comand == 'save & exit':
        save_notes(notes)
    elif comand != 'exit':
        print('Не коректне введення. Виберіть: add, earliest, latest, longest, shortest')


if __name__ == '__main__':
    comand_ = ''
    notes_ = load_notes()
    while comand_ != 'exit':
        comand_ = input_comand()
        exec_comand(comand_, notes_)
