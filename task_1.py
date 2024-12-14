from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Абстрактный класс для транспортных средств.

    Атрибуты:
        model (str): Модель транспортного средства.
        year (int): Год выпуска.
    """

    def __init__(self, model: str, year: int):
        if year < 1886:  # Первый автомобиль был создан в 1886
            raise ValueError("Год выпуска не может быть раньше 1886.")
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self) -> str:
        """Запускает двигатель транспортного средства.

        Returns:
            str: Сообщение о запуске двигателя.

        >>> v = Car("Toyota", 2020)
        >>> v.start_engine()
        'Двигатель Toyota запущен.'
        """
        pass

    @abstractmethod
    def stop_engine(self) -> str:
        """Останавливает двигатель транспортного средства.

        Returns:
            str: Сообщение о остановке двигателя.
        """
        pass


class Animal(ABC):
    """Абстрактный класс для животных.

    Атрибуты:
        species (str): Вид животного.
        age (int): Возраст животного.
    """

    def __init__(self, species: str, age: int):
        if age < 0:
            raise ValueError("Возраст животного не может быть отрицательным.")
        self.species = species
        self.age = age

    @abstractmethod
    def make_sound(self) -> str:
        """Издает звук, характерный для животного.

        Returns:
            str: Звук животного.

        >>> a = Dog("Собака", 3)
        >>> a.make_sound()
        'Гав!'
        """
        pass

    @abstractmethod
    def eat(self, food: str) -> str:
        """Кормит животное.

        Args:
            food (str): Вид корма.

        Returns:
            str: Сообщение о кормлении.
        """
        pass


class ElectronicDevice(ABC):
    """Абстрактный класс для электронных устройств.

    Атрибуты:
        brand (str): Бренд устройства.
        model (str): Модель устройства.
    """

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @abstractmethod
    def power_on(self) -> str:
        """Включает устройство.

        Returns:
            str: Сообщение о включении устройства.

        >>> ed = Phone("Apple", "iPhone 13")
        >>> ed.power_on()
        'iPhone 13 включен.'
        """
        pass

    @abstractmethod
    def power_off(self) -> str:
        """Выключает устройство.

        Returns:
            str: Сообщение о выключении устройства.
        """
        pass


# Пример наследования и реализации
class Car(Vehicle):
    def start_engine(self) -> str:
        return f"Двигатель {self.model} запущен."

    def stop_engine(self) -> str:
        return f"Двигатель {self.model} остановлен."


class Dog(Animal):
    def make_sound(self) -> str:
        return "Гав!"

    def eat(self, food: str) -> str:
        return f"{self.species} кушает {food}."


class Phone(ElectronicDevice):
    def power_on(self) -> str:
        return f"{self.model} включен."

    def power_off(self) -> str:
        return f"{self.model} выключен."


if __name__ == "__main__":
    import doctest
    doctest.testmod()

