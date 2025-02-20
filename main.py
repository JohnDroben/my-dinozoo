##Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.



class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):

    def make_sound(self):
        print("Птицы щебечут")

    def eat(self):
        print("Птицы клюют зерно")


class Mammal(Animal):

    def make_sound(self):
        print("Звери рычат")

    def eat(self):
        print("Звери едят мясо")



class Reptile(Animal):

    def make_sound(self):
        print("Рептилии шипят")

    def eat(self):
        print("Рептилии едят траву")




animals = [Bird("Соловей", 2), Mammal("Тигр", 3), Reptile("Нагайна", 8)]

for animal in animals:
           animal.make_sound()

for animal in animals:
           animal.eat()



