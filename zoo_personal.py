#4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).
# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import pickle
from main import Animal
from main import animal
from main import Bird
from main import Mammal
from abc import ABC, abstractmethod

class Staff():
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def work(self):
        pass

class ZooKeeper(Staff):
    def work(self):
        print(f"{self.name} кормит животных")

    def feed_animal(self):
        print(f"{self.name} кормит {animal.name}")

class Veterinarian (Staff):
    def work(self):
        print(f"{self.name} лечит животных")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}")


class Zoo():
    def __init__(self):
        self._animals = []
        self._staff = []
        pass

    def add_animals(self):
        if isinstance(animal, Animal):
            self._animals.append(animal)
        else:
            raise ValueError("Можно добавлять только животных")

    def add_employee(self, employee):
        if isinstance(employee, Staff):
            self._staff.append(employee)
        else:
            raise ValueError("Можно добавлять только сотрудников")

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
    parrot = Bird("Попугай Кеша", 3)
    tiger = Mammal("Тигр Барсик", 5)
    keeper = ZooKeeper("Иван Петров")
    vet = Veterinarian("Мария Иванова")

    # Добавление в зоопарк сотрудников

    zoo.add_employee(keeper)
    zoo.add_employee(vet)

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