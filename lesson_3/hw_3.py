# 1. Користувач вводить строку
# 2. Програма переводить строку в нижній регістр
# 3. Програма видаляє зі строки такі символи пунктуації: .,-:;?!
# 4. Програма видаляє зайві пробіли\табуляції з правого кінця строки
# 5. Програма питає користувача яке слово (або словосполучення) він бажає замінити
# 6. Програма повідомляє на якому індексі строки словосполучення присутнє
# 7. Програма питає на яке слово треба замінити
# 8. Програма виводить відформатовану строку

# 1. Користувач вводить строку
program_str = str(input('Please, input your string: '))
# 2. Програма переводить строку в нижній регістр
res = str.lower(program_str)

# 3. Програма видаляє зі строки такі символи пунктуації: .,-:;?!
replacements = [
    (".", ""),
    (",", ""),
    ("-", ""),
    (":", ""),
    (";", ""),
    ("?", ""),
    ("!", "")
    # (")", ""),
    # ("(", "")
]
for old, new in replacements:
    res = res.replace(old, new)

# 4. Програма видаляє зайві пробіли\табуляції з правого кінця строки
res = str.rstrip(res)

# 5. Програма питає користувача яке слово (або словосполучення) він бажає замінити
program_found = str(input('What do you want to replace?: '))
program_found = str.lower(program_found)

# 6. Програма повідомляє на якому індексі строки словосполучення присутнє
index = res.find(program_found)
if index != -1:
    print(f"'{program_found}' was found at position {index}!")
else:
    print(f"'{program_found}' not found")

# 7. Програма питає на яке слово треба замінити
if index != -1:
    program_change = str(input('With what do you want to replace?: '))
    program_change = str.lower(program_change)
    res = res.replace(program_found, program_change)
# 8. Програма виводить відформатовану строку
    print(res)
else:
    print('end')
