#Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке
# в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние"
# между запусками программы.

import pickle
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} ест.")

class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает: Чик-чирик!")

class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит: Рррр!")

class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит: Шшссс!")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

class ZooKeeper(Employee):
    def work(self):
        print(f"{self.name} кормит животных")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian(Employee):
    def work(self):
        print(f"{self.name} лечит животных")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")

class Zoo:
    def __init__(self):
        self._animals = []
        self._staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)
        else:
            raise TypeError("Можно добавлять только животных")

    def add_staff(self, employee):
        if isinstance(employee, Employee):
            self._staff.append(employee)
        else:
            raise TypeError("Можно добавлять только сотрудников")

    def show_animals(self):
        return [animal.name for animal in self._animals]

    def show_staff(self):
        return [employee.name for employee in self._staff]

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump((self._animals, self._staff), f)

    @classmethod
    def load_from_file(cls, filename):
        zoo = cls()
        try:
            with open(filename, 'rb') as f:
                animals, staff = pickle.load(f)
                zoo._animals = animals
                zoo._staff = staff
        except FileNotFoundError:
            print("Файл не найден, создан новый зоопарк")
        return zoo

# Пример использования
if __name__ == "__main__":
    # Создание объектов
    zoo = Zoo()
    parrot = Bird("Попугай Кеша", 3, 30)
    tiger = Mammal("Тигр Барсик", 5, "Оранжевый")
    snake = Reptile("Змея Каа", 2, "Крупная чешуя")

    keeper = ZooKeeper("Иван Петров")
    vet = Veterinarian("Мария Иванова")

    # Добавление в зоопарк
    zoo.add_animal(parrot)
    zoo.add_animal(tiger)
    zoo.add_animal(snake)
    zoo.add_staff(keeper)
    zoo.add_staff(vet)

    # Демонстрация полиморфизма
    print("\nЗвуки животных:")
    animal_sound(zoo._animals)

    # Работа сотрудников
    print("\nРабота сотрудников:")
    keeper.feed_animal(tiger)
    vet.heal_animal(parrot)

    # Сохранение состояния
    zoo.save_to_file("zoo.dat")

    # Загрузка состояния
    new_zoo = Zoo.load_from_file("zoo.dat")
    print("\nЗагруженные животные:", new_zoo.show_animals())
    print("Загруженные сотрудники:", new_zoo.show_staff())