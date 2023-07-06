from .animal import Animal


class Cat(Animal):
    # init так же называют конструктором класса
    def __init__(self, name: str, age: int, say_word='Мяу!'):
        """
        Класс отвечает за симуляцию животного кота
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'корм сухой', 'корм мокрый', 'рыба', 'мясо'}

        )
        self.animal_type = 'Кот'

    def treat(self, hours: int) -> str:
        """
        Ухаживая за котом должное количество времени, мы получаем ласку
        :param hours: время ухаживания
        :return: ласка или ничего
        """
        if hours > 1:
            print(f'Вы ухаживаете за {self} {hours} часов и получаете мурлыкание')
            return 'Мурлыкание'
        print(f'Вы ухаживаете за {self} {hours} часов.')
        return ''
