simvol = input('simvol: ')
number = int(input('number: '))

print('line:')
# команда рисования линии
for _ in range(number): # для каждого элемента
    print(simvol, end='') # на каждую итерацию что хотим сделать
print()
# конец команды рисования линии

print('square:')
# команда рисования квадрата
for _ in range(number):
    for _ in range(number):  # для каждого элемента
        print(simvol, end='')  # на каждую итерацию что хотим сделать
    print()
# конец команды рисования квадрата

print()
print('triangle:')
# команда рисования треугольника
for i in range(number):
    for j in range(i):
        print(simvol, end='')
        # print(i, j)
    print()
# конец команды рисования треугольника

# нарисовать треугольник
# нарисовать равнобедренный треугольник
# нарисовать елочку из равнобедренных треугольников
# нарисовать 3 фигуры с помощью while

# чем отличается
x = [2, 3, 4]
new_x = list()
for element in x:
    new_x.append(element + 3)
print(new_x)

x = [2, 3, 4]
for element in x:
    element += 3
print(x)

# как вводить в инпут перенос строки?