"""
Написати клас кішка (Cat), схожий до класу собака (Dog) з запису заняття та доповнити його,
продемонструвавши відомі можливості ООП.

Реалізувати наступні методи/поведінку в повсякденному житті кішок:
Їсти
Гуляти
Мяукати
Створити якнайменше 6 об'єктів класу кішка (представників) рандомною генерацією чи вписати в код (можна читати з файлу,
але краще уникати введення від користувача - так на користування програмою витрачається забагато часу).

Включити перевірку кожного дня:
Чи кішка гуляла
Чи кішка їла
Оцінювання
60/60 коректність структури класу кішка
30/30 коректність створення класу кішка та його використання
(без global scope, у __main__, а ще краще - у іншому файлі, куди клас імпортується)
5/5 наявність коментарів
5/5 відсутність ПЕП зауважень
+? творчий підхід, тут його багато :)
"""
from random import choices, randint, random


class Cat:
    def __init__(self, name: str, age: int, breed: str, preferred_food: set):
        """
        Класс кошка
        :param name: имя
        :param age: возраст
        :param breed: порода
        :param preferred_food: предпочитаемая еда
        """
        self.name = name
        self.age = age
        self.breed = breed
        self.preferred_food = preferred_food
        self.hungry = True
        self.hours_outdoors = 0
        self.hours_sleep = 0

    def __str__(self):
        starting_str = f"{self.breed.capitalize()} {self.name}, возраст: {self.age} "
        starting_str += f", часов гулял: {self.hours_outdoors}, спал: {self.hours_sleep}, голоден: {self.hungry}"
        return starting_str

    def mew(self, count: int):
        if count > 0:
            barking_str = '-'.join(["мяу"] * count).capitalize()
            print(f"{self.name} мяукает: {barking_str}!")

    def eat(self, food: str):
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name} кушает {food}")
                self.hungry = False
            else:
                print(f"{self.name} такое не ест: {food}")
                self.mew(randint(1, 5))
        else:
            print(f"{self.name} не голоден")

    def sleep(self, tired: bool):
        if tired:
            hours = randint(2, 5)
            print(f"{self.name} спит {hours} часов")
            self.hours_sleep += hours
        else:
            print(f"{self.name} не хочет спать")
        if self.hours_sleep > 3:
            self.hungry = True
        return "Хорошо себя чувствует!" if not None else tired

    def walk(self, alone: bool):
        """
        Кошка гуляет
        :param alone: если True, то собака гуляет одна, если False - то с хозяином
        Если кошка гуляла суммарно больше 3 часов, то она проголодалась
        :return: если с хозяином - повышается настроение (у хозяина), если сама - None
        """
        if alone:
            hours = randint(2, 4)
            with_str = "сам"
        else:
            hours = randint(1, 2)
            with_str = "с хозяином"
        print(f"{self.name} гуляет {with_str} {hours} часа")
        self.hours_outdoors += hours
        if self.hours_outdoors > 3:
            self.hungry = True
        # """то же самое, что ниже, но проще читать
        #         if alone:
        #             return
        #         else:
        #             return "Хорошее настроение!"
        #         """
        return "Хорошее настроение!" if not alone else None


if __name__ == '__main__':
    # Как передавать значения в класс и делать объекты разными
    d = Cat('Бакс', 2, "британец", {'каша'})
    x = Cat('Нюся', 4, "простая", {'рыба', 'хлеб'})
    y = Cat('Снежок', 3, "сиамский", {'рыба', 'мясо', 'каша'})
    z = Cat('Филя', 5, "мейн-кун", {'рыба', 'борщ', 'сало'})
    a = Cat('Фараон', 5, "сфинкс", {'рыба', 'борщ', 'сало'})
    b = Cat('Том', 5, "бенгал", {'рыба', 'борщ', 'сало'})

    cats = [d, x, y, z, a, b]
    print(d.name, x.name, y.name, z.name, a.name, b.name)
    print(d)
    print(x)
    print(y)
    print(z)

    potential_food = ['каша', 'корм сухой', 'рыба', 'суп', 'сало', 'корм', 'яблоко']
    print('Обычный день в жизни одной кошки :)')
    print('-' * 40)
    for cat in cats:
        events_for_cat = randint(1, 8)
        for _ in range(events_for_cat):
            if random() > 0.5:
                print(f'Кормим {cat.name}')
                for random_food in choices(potential_food, k=3):
                    cat.eat(random_food)
                if random() > 0.5:
                    result = cat.sleep(tired=True)
                    print(f"Кот {result}")
                else:
                    result = cat.sleep(tired=False)
            else:
                if random() > 0.5:
                    result = cat.walk(alone=True)
                else:
                    result = cat.walk(alone=False)
                print(f'После прогулки хозяин понял, что: {result}')
        print(f'Прошел день для: {cat}')
        print('=' * 50)
