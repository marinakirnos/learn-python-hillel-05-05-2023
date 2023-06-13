d = {
    "Monitors": 3,
    "Keyboard": 4,
    "Headset": 6,
    "Laptop": 2
}


def dict_element_getter(element):
    print(element, type(element))
    # то что return-ит функция из key будет использовано для сортировки
    return element[1]


# Словарь можно создать "легко" из списка парных кортежей.
# Первый элемент кортежа станет ключом, второй - значением
sorted_dictionary = dict(sorted(d.items(), key=dict_element_getter))
print(sorted_dictionary, type(sorted_dictionary))

# lambda-функции это так называемые однострочные, простые, анонимные функции
# у них нет имени они не рассчитаны на повторные вызовы

# lambda <входные параметры через запятую>: <что функция возвращает>
# lambda element: element[1]
print('Lambda sorting')
sorted_dictionary = dict(sorted(d.items(), key=lambda element: element[1]))
print(sorted_dictionary, type(sorted_dictionary))
