"""
Вправа на індекси
Надано файл tech_inventory.csv з товарами інтернет-магазину техніки. Що відомо про кожну позицію (заголовки файлу):
model
category
brand
price
Треба написати програму що:

читає цей файл
створює індекс унікальних айді для кожного запису, тобто словник, де ключі - це згенеровані унікальні айді,
а значення - повна інформація про позицію товару
створює індекс по категоріям та брендам. Тобто словник, де ключі - це назва категорії/бренду, а значення -
це перелік унікальних айді товарів, в яких є таке значення поля категорії/бренду
виводить на екран статистику скільки товарів є від кожного бренда та від кожної категорії
виводить на екран перелік повної інформації про кожний товар одного обраного бренда та однієї обраної категорії
рахує розподіл товарів по брендам для кожної категорії та виводить це на екран. Наприклад, в категорії Ноутбуки
представлено 6 товарів від Lenovo, 8 від Mac, 10 від Dell, тощо.
"""


import csv


def open_csv_file_dict(filename, to_print=True) -> list:
    """
    Функция читает ряды csv файла как dict (с заголовками),
     возвращает их и выводит на экран при надобности
    :param filename: путь к файлу, который нужно открыть
    :param to_print: флаг выводить ли на экран
    :return: возвращаем содержимое файла списком рядов,
             каждый ряд - словарь,
             ключи словаря - заголовки csv файла
    """
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        if to_print:
            print(type(reader), reader)
            for row in rows:
                print(type(row), row)
        return rows


def create_index(all_data: list, column_name: str) -> dict:
    """
    В этой функции создаётся индекс по колонке, чьё имя мы указываем
    :param all_data: данные в которых находятся колонки из которых мы строим индекс.
                    Данные представлены в виде список словарей
    :param column_name: имя колонки, по которой построить индекс
    :return: индекс, т.е. словарь,
            где ключи - это уникальные значения из колонки column_name,
            а значения под ключами - это список записей из all_data,
            у которых есть такое значение в column_name
    """
    new_index = dict()
    for data_entry in all_data:
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(data_entry)
    return new_index


def create_position_id_index(all_data, column_name: str) -> dict:
    new_index = dict()
    for i, data_entry in enumerate(all_data):
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(i)
    return new_index


def print_position_id_index(all_data: list, position_index: dict):
    for index_key, position_values in position_index.items():
        print(f'Записи со значением {index_key}')
        for i in position_values:
            print('  ', all_data[i])


if __name__ == '__main__':
    tech_inventory_data = open_csv_file_dict('tech_inventory.csv', to_print=True)

    category_index = create_index(tech_inventory_data, 'category')
    print(type(category_index), category_index)


    category_position_id_index = create_position_id_index(tech_inventory_data, 'category')
    print(type(category_position_id_index), category_position_id_index)
    print_position_id_index(tech_inventory_data, category_position_id_index)

    brand_index = create_index(tech_inventory_data, 'brand')
    print(type(brand_index), brand_index)