# функция полиморфизм -> len(): __len__
# print(len('Makers'))

# + (__add__) -  метод
# print(5 + 5)
# print('hello' + 'world')

# Полиморфизм - способнсоть функции(мктода) исполтзоватся для разных типов(кдвссов)
# Широко распрастранненое определение:"один игтерфейс - много реализаций"
# list.pop
# set.pop
# dict.pop

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a cat. Cats  name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('miay, miay')



# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'It\'s a dog. Dog  name is {self.name}, age: {self.age}')

#     def make_sound(self):
#         print('brak, brak')

# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 6)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(aelf):
#         pass

#     @abstractmethod
#     def fact(self):
#         pass

# class Square(Shape):
#     def __init__(self, lenght) -> None:
#         super().__init__('Квадрат')
#         self.lenght = lenght

#     def area(self):
#         return self.lenght ** 2
    
#     def fact(self):
#         return 'У квадрата все стороны равны и углы равны 90 градусом!'
    
# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Окружность')
#         self.radius = radius

#     def area(self):
#         from math import pi
#         return pi * self.radius ** 2
    
#     def fact(self):
#         return 'Окружность- это множество точек плоскостиб расстояние которых до данной точки (центра окружности) лдинаково'
    
# a = Square(5)
# b = Circle(5)
# print(a.area())
# print(b.area())

