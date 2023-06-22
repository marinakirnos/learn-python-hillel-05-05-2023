import csv

def open_csv_file_dict(filename, to_print=True):
    with open(filename, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)
        if to_print:
            print(type(reader), reader)
            for row in rows:
                print(type(row), row)
        return rows

def create_index(all_data, column_name: str) -> dict:
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
    children_data = open_csv_file_dict('children.csv', to_print=False)

    # unique id (в качестве ссылок на данные, чтобы их не дублировать
    # дублирование чревато дополнительным занимаемым местом,
    # а так же неконсистентность редактирования данных
    # (редактировании одной копии не редактирует остальные)
    # консистентность в этом примере работает, однако при разделении
    # на разные файлы может не работать
    print(children_data[4])

    age_index = create_index(children_data, 'age')
    print(type(age_index), age_index)


    age_position_id_index = create_position_id_index(children_data, 'age')
    print(type(age_position_id_index), age_position_id_index)
    print_position_id_index(children_data, age_position_id_index)

    group_index = create_index(children_data, 'group')
    print(type(age_index), group_index)