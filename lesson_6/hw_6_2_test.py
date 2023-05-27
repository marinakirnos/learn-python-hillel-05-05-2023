pattern = list()
result = ""
# text = input("Введіть звернення: ")

while True:
    text = input("Введіть звернення: ")  # Користувач вводить текст
    # перевірка що текст не пустий
    if text != '':
        try:
            for simvol in text:
                if simvol == '(':
                    pattern.append('(')
                elif simvol == ')':
                    if pattern:
                        pattern.pop()
                elif not pattern:
                    result += simvol
        except Exception:
            print('Строка не повинна бути пустою')
        break
    # else:
    #     print('Строка не повинна бути пустою')
print(result)

# print(result)
# print(pattern)


# Приклад використання
# text = "Це (текст) з (декількома) дужками."
