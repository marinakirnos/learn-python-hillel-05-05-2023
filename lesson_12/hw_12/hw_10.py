"""
Вправа на індекси
Надано файл tech_inventory.csv з товарами інтернет-магазину техніки. Що відомо про кожну позицію (заголовки файлу):
model
category
brand
price
Треба написати програму що:
- читає цей файл
- створює індекс унікальних айді для кожного запису, тобто словник, де ключі - це згенеровані унікальні айді,
а значення - повна інформація про позицію товару
- створює індекс по категоріям та брендам. Тобто словник, де ключі - це назва категорії/бренду, а значення -
це перелік унікальних айді товарів, в яких є таке значення поля категорії/бренду
- виводить на екран статистику скільки товарів є від кожного бренда та від кожної категорії
- виводить на екран перелік повної інформації про кожний товар одного обраного бренда та однієї обраної категорії
- рахує розподіл товарів по брендам для кожної категорії та виводить це на екран. Наприклад, в категорії Ноутбуки
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


def create_index(all_data: list) -> dict:
    """
    В этой функции создаётся индекс уникального значения для каждой записи
    :param all_data: данные. Данные представлены в виде список словарей
    :return: индекс, т.е. словарь,
            где ключи - это айди,
            а значения под ключами - это уникальные записи
    """
    new_index = dict()
    unique_id = 1
    for row in all_data:
        new_index[unique_id] = row
        unique_id += 1
    return new_index


def create_category_brand_index_key(record: dict):
    """
    Функция выбирает категории и бренды
    :param record: словник, ключ -  id товар, значения под ключами - это уникальные записи
    :return: сочитание категории и бренда
    """
    return tuple(sorted({'category': record['category'].lower(), 'brand': record['brand'].lower()}.items()))


def create_category_brand_dict(records: dict):
    """
    створює індекс по категоріям та брендам. Тобто словник, де ключі - це назва категорії/бренду, а значення -
    це перелік унікальних айді товарів, в яких є таке значення поля категорії/бренду
    :param records: словник, ключ -  id товар, значения под ключами - это уникальные записи
    :return:
    """
    category_brand_dict = dict()
    for key in records.keys():
        category_brand_index_key = create_category_brand_index_key(records[key])
        if category_brand_index_key in category_brand_dict:
            category_brand_dict[category_brand_index_key].append(key)
        else:
            category_brand_dict[category_brand_index_key] = [key]
    return category_brand_dict


def create_position_id_index(all_data, column_name: str) -> dict:
    """
    Статистика скільки товарів є від кожної категорії:
    :param all_data: данные. Данные представлены в виде список словарей
    :param column_name: название колонки по какой хотим группировать: категории, бренд
    :return: Перечень категорий и кол-во товаров, перечень брендов и кол-во товаров
    """
    new_index = dict()
    for i, data_entry in enumerate(all_data):
        if data_entry[column_name] not in new_index:
            new_index[data_entry[column_name]] = list()
        new_index[data_entry[column_name]].append(i)
    return new_index


def print_create_position_category_brand(position_index: dict):
    for index_key, position_values in position_index.items():
        print(f'Записи {index_key},', position_values)


def print_position_id_index(position_index: dict):
    for index_key, position_values in position_index.items():
        print(f'Записи со значением {index_key}:', len(position_values))


def category_brand_items(category_brand_dict: dict, id_index: dict, category: str, brand: str):
    """
    Виводить на екран перелік повної інформації про кожний товар одного бренда та однієї категорії:
    :param category_brand_dict:  словник, де ключі - це назва категорії/бренду, а значення -
    це перелік унікальних айді товарів, в яких є таке значення поля категорії/бренду
    :param id_index: индекс, т.е. словарь,
            где ключи - это айди товара,
            а значения под ключами - это уникальные записи (повна інформація про товар
    :param category: категория
    :param brand: бренд
    :return: перелік повної інформації про кожний товар одного бренда та однієї категорії
    """
    key = create_category_brand_index_key({'brand': brand, 'category': category})
    id_list = category_brand_dict[key]
    detailed_prodact_list = []
    for id_ in id_list:
        detailed_prodact_list.append(id_index[id_])
    return detailed_prodact_list


def category_brand_items_count(all_data: dict):
    """
    Рахує розподіл товарів по брендам для кожної категорії та виводить це на екран
    :param all_data: записи по товару
    :return: Кол-во товаров по брендам в каждой категории
    """
    count_brand_for_category = {}
    for product in all_data.values():
        category = product['category']
        brand = product['brand']
        if category not in count_brand_for_category:
            count_brand_for_category[category] = {}
        if brand not in count_brand_for_category[category]:
            count_brand_for_category[category][brand] = 0
        count_brand_for_category[category][brand] += 1
    return count_brand_for_category


if __name__ == '__main__':
    print('Читає цей файл:')
    tech_inventory_data = open_csv_file_dict('tech_inventory.csv', to_print=False)
    print(tech_inventory_data)

    print()
    print('Створює індекс унікальних айді для кожного запису:')
    tech_inventory_index = create_index(tech_inventory_data)
    print(type(tech_inventory_index), tech_inventory_index)
    for index_key_, position_values_ in tech_inventory_index.items():
        print(f'ID {index_key_},', position_values_)

    print()
    print('Створює індекс по категоріям та брендам:')
    category_brand = create_category_brand_dict(tech_inventory_index)
    print(category_brand)
    print_create_position_category_brand(category_brand)

    print()
    print('Статистика скільки товарів є від кожної категорії:')
    category_position_id_index = create_position_id_index(tech_inventory_data, 'category')
    # print(type(category_position_id_index), category_position_id_index)
    print_position_id_index(category_position_id_index)

    print()
    print('Статистика скільки товарів є від кожного бренда:')
    brand_position_id_index = create_position_id_index(tech_inventory_data, 'brand')
    # print(type(brand_position_id_index), brand_position_id_index)
    print_position_id_index(brand_position_id_index)

    print()
    print('Виводить на екран перелік повної інформації про кожний товар одного бренда та однієї категорії:')
    items_brand_category = category_brand_items(category_brand, tech_inventory_index, 'laptop', 'hp')
    for item in items_brand_category:
        print(item)

    print()
    print('Рахує розподіл товарів по брендам для кожної категорії та виводить це на екран:')
    category_brand_items_count_ = category_brand_items_count(tech_inventory_index)
    for category_ in category_brand_items_count_.keys():
        print(category_)
        for brand_ in category_brand_items_count_[category_].keys():
            print('\t', brand_, category_brand_items_count_[category_][brand_])

    # for category in category_brand_items_count_.keys():
    #     for brand in category_brand_items_count_[category].keys():
    #         print(category, brand, category_brand_items_count_[category][brand])
