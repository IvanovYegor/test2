# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Table:
    def __init__(self, material: str, length: float, width: float):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал стола
        :param length: Длина стола
        :param width: Ширина стола

        Пример:
        >>> table = Table("дерево", 100, 60)  # инициализация экземпляра класса
        """
        if not material:
            raise ValueError("Материал не может быть пустым.")
        if length <= 0:
            raise ValueError("Длина стола должна быть положительным числом.")
        if width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом.")
        self.attr1 = material
        self.attr2 = length
        self.attr3 = width

    def area(self) -> float:
        """
        Рассчитывает площадь стола

        Пример:
        >>> table = Table("дерево", 100, 60)
        >>> table.area()
        6000
        """
        ...
        return self.attr2 * self.attr3

    def describe(self) -> str:
        """
        Формирует описание стола

        Пример:
        >>> table = Table("дерево", 100, 60)
        >>> table.describe()
        'Стол из материала дерево размером 100 см на 60 см.'
        """
        ...
        return f"Стол из материала {self.attr1} размером {self.attr2} см на {self.attr3} см."


class Car:
    def __init__(self, brand: str, model: str, max_speed: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Бренд автомобиля
        :param model: Модель автомобиля
        :param max_speed: Максимальная скорость автомобиля

        Пример:
        >>> car = Car("Suzuki", "Vitara", 200)  # инициализация экземпляра класса
        """
        if not brand:
            raise ValueError("Бренд не может быть пустым.")
        if not model:
            raise ValueError("Модель не может быть пустой.")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом.")
        self.attr1 = brand
        self.attr2 = model
        self.attr3 = max_speed

    def describe(self) -> str:
        """
        Формирует описание автомобиля

        Пример:
        >>> car = Car("Suzuki", "Vitara", 200)
        >>> car.describe()
        'Автомобиль Suzuki Vitara, максимальная скорость 200 км/ч.'
        """
        ...
        return f"Автомобиль {self.attr1} {self.attr2}, максимальная скорость {self.attr3} км/ч."

    def accelerate(self, increase: float) -> float:
        """
        Увеличивает максимальную скорость автомобиля

        Пример:
        >>> car = Car("Suzuki", "Vitara", 200)
        >>> car.accelerate(20)
        220
        >>> car.accelerate(-10)  # Это вызовет ValueError
        Traceback (most recent call last):
        ...
        ValueError: Увеличение скорости должно быть положительным числом.
        """
        ...
        if increase <= 0:
            raise ValueError("Увеличение скорости должно быть положительным числом.")
        self.attr3 += increase
        return self.attr3


class Telegram:
    def __init__(self, username: str, phone_number: str, messages: list = None):
        """
        Создание и подготовка к работе объекта "Telegram"

        :param username: Имя пользователя
        :param phone_number: Номер телефона
        :param messages: Сообщение пользователю

        Пример:
        >>> telegram = Telegram("User27", "8212323231")  # инициализация экземпляра класса
        """
        if not username:
            raise ValueError("Имя пользователя не может быть пустым.")
        if not phone_number:
            raise ValueError("Номер телефона не может быть пустым.")
        self.attr1 = username
        self.attr2 = phone_number
        self.attr3 = messages if messages is not None else []

    def send_message(self, message: str) -> None:
        """
        Отправляет сообщение пользователю

        Пример:
        >>> telegram = Telegram("User27", "8212323231")
        >>> telegram.send_message("Привет!")
        >>> telegram.attr3
        ['Привет!']
        >>> telegram.send_message("")  # Это вызовет ValueError
        Traceback (most recent call last):
        ...
        ValueError: Сообщение не может быть пустым.
        """
        ...
        if not message:
            raise ValueError("Сообщение не может быть пустым.")
        self.attr3.append(message)

    def describe(self) -> str:
        """
        Формирует описание пользователя

        Пример:
        >>> telegram = Telegram("User27", "8212323231")
        >>> telegram.describe()
        'Пользователь User27 с номером телефона 8212323231.'
        """
        ...
        return f"Пользователь {self.attr1} с номером телефона {self.attr2}."


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass

