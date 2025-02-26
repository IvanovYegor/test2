class Animal:
    """
    Базовый класс для животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Инициализация животного.

        :param name: Название животного.
        :param age: Возраст животного.
        """
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        """Возвращает имя животного."""
        return self._name

    @property
    def age(self) -> int:
        """Возвращает возраст животного."""
        return self._age

    def speak(self) -> str:
        """
        Метод, который возвращает звук, издаваемый животным.
        По умолчанию возвращает 'Some sound'.

        :return: Звук, издаваемый животным.
        """
        return "Some sound"

    def __str__(self) -> str:
        """Возвращает строковое представление животного."""
        return f"Animal(name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление животного."""
        return f"Animal('{self.name}', {self.age})"


class Dog(Animal):
    """
    Класс для собак, наследующий от класса Animal.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Инициализация собаки.

        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)  # Вызов конструктора базового класса
        self._breed = breed

    @property
    def breed(self) -> str:
        """Возвращает породу собаки."""
        return self._breed

    def speak(self) -> str:
        """
        Метод, который возвращает звук, издаваемый собакой.
        Переопределяет метод speak базового класса.

        :return: Звук, издаваемый собакой.
        """
        return "Woof!"

    def __str__(self) -> str:
        """Возвращает строковое представление собаки."""
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def __repr__(self) -> str:
        """Возвращает официальное строковое представление собаки."""
        return f"Dog('{self.name}', {self.age}, '{self.breed}')"


if __name__ == "__main__":
    # Write your solution here
    animal = Animal("Generic Animal", 5)
    print(animal)  # Animal(name=Generic Animal, age=5)
    print(repr(animal))  # Animal('Generic Animal', 5)

    dog = Dog("Buddy", 3, "Golden Retriever")
    print(dog)  # Dog(name=Buddy, age=3, breed=Golden Retriever)
    print(repr(dog))  # Dog('Buddy', 3, 'Golden Retriever')
    print(dog.speak())  # Woof!
    pass

