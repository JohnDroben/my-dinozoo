# Проект: Зоопарк с использованием ООП и принципов SOLID

## Описание проекта

Проект представляет собой имитацию работы зоопарка, используя объектно-ориентированный подход. В нем реализованы основные концепции ООП: наследование, полиморфизм, абстракция и композиция. Также включена возможность сохранения состояния зоопарка между запусками программы.

Основная цель — создать гибкую систему управления животными и сотрудниками зоопарка, которая может легко расширяться и поддерживать постоянное состояние.

---

## Структура проекта

### 1. Базовый класс `Animal`

Класс `Animal` является базовым для всех животных. Он содержит общие атрибуты и методы:

- **Атрибуты**:
  - `name`: Имя животного.
  - `age`: Возраст животного.

- **Методы**:
  - `make_sound()`: Абстрактный метод для воспроизведения звука животного.
  - `eat()`: Метод, который показывает, что животное ест.

```python
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
```

---

### 2. Подклассы животных

#### Класс `Bird`
Представляет птиц. Добавляет специфический атрибут `wing_span` (размах крыльев) и переопределяет метод `make_sound()`.

```python
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает: Чик-чирик!")
```

#### Класс `Mammal`
Представляет млекопитающих. Добавляет атрибут `fur_color` (цвет шерсти) и переопределяет метод `make_sound()`.

```python
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит: Рррр!")
```

#### Класс `Reptile`
Представляет рептилий. Добавляет атрибут `scale_type` (тип чешуи) и переопределяет метод `make_sound()`.

```python
class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит: Шшссс!")
```

---

### 3. Полиморфизм

Функция `animal_sound(animals)` демонстрирует полиморфизм: она принимает список животных и вызывает метод `make_sound()` для каждого из них.

```python
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
```

Пример использования:

```python
parrot = Bird("Попугай Кеша", 3, 30)
tiger = Mammal("Тигр Барсик", 5, "Оранжевый")
snake = Reptile("Змея Каа", 2, "Крупная чешуя")

print("\nЗвуки животных:")
animal_sound([parrot, tiger, snake])
```

---

### 4. Композиция: Класс `Zoo`

Класс `Zoo` управляет животными и сотрудниками зоопарка. Он включает методы для добавления новых элементов и просмотра текущего состава.

- **Атрибуты**:
  - `_animals`: Список животных.
  - `_staff`: Список сотрудников.

- **Методы**:
  - `add_animal(animal)`: Добавляет новое животное.
  - `add_staff(employee)`: Добавляет нового сотрудника.
  - `show_animals()`: Возвращает список имён животных.
  - `show_staff()`: Возвращает список имён сотрудников.
  - `save_to_file(filename)`: Сохраняет состояние зоопарка в файл.
  - `load_from_file(filename)`: Загружает состояние зоопарка из файла.

```python
import pickle

class Zoo:
    def __init__(self):
        self._animals = []
        self._staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)
        else:
            raise TypeError("Можно добавлять только животных.")

    def add_staff(self, employee):
        if isinstance(employee, Employee):
            self._staff.append(employee)
        else:
            raise TypeError("Можно добавлять только сотрудников.")

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
            print("Файл не найден. Создан новый зоопарк.")
        return zoo
```

---

### 5. Классы сотрудников

#### Класс `Employee`
Базовый класс для всех сотрудников. Содержит абстрактный метод `work()`.

```python
class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def work(self):
        pass
```

#### Класс `ZooKeeper`
Представляет держателя зоопарка. Имеет метод `feed_animal()` для кормления животных.

```python
class ZooKeeper(Employee):
    def work(self):
        print(f"{self.name} кормит животных.")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")
```

#### Класс `Veterinarian`
Представляет ветеринара. Имеет метод `heal_animal()` для лечения животных.

```python
class Veterinarian(Employee):
    def work(self):
        print(f"{self.name} лечит животных.")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")
```

---

### 6. Пример использования

```python
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
```

---

## Функциональность проекта

1. **Создание и управление животными**: Можно создавать различные виды животных, добавлять их в зоопарк и просматривать список.
2. **Сотрудники зоопарка**: Поддерживаются разные роли (например, дежурный зоопарка и ветеринар) с уникальными действиями.
3. **Полиморфизм**: Все животные могут издавать свои уникальные звуки через общий интерфейс.
4. **Сохранение состояния**: Информация о зоопарке сохраняется в файле, позволяя восстанавливать её при следующем запуске программы.

---

## Преимущества архитектуры

1. **Гибкость**: Легко добавлять новые типы животных или сотрудников без изменения существующего кода.
2. **Чистота кода**: Использование абстракций и наследования делает код более организованным и понятным.
3. **Постоянное состояние**: Возможность сохранения и загрузки данных обеспечивает непрерывность работы программы.

---
