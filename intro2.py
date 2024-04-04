# class Student:
#     univer = 'MIT'

#     def __init__(self, name) -> None:
#         self.name = name
#         self.books = []
#         self.language = {}
#         self.knowledge = 0
#         self.is_ready_work = False

#     def add_points(self, point):
#         if self.knowledge > 500 and not self.is_ready_work:
#             self.is_ready_work = True
#             print(f'{self.name} gets 500 points and ready to work')

#     def read_book(self, book_name):
#         self.add_points(50)
#         self.books.append(book_name)

#     def do_project(self):
#         self.add_points(100)

#     def learn_lang(self, language, precent):
#         if precent not in range(70, 101):
#          print('invalid points for lang!!!')
#         else:
#             self.language[language] = precent
#             self.add_points(precent)

# st1 = Student('Maikl')
# st2 = Student('Din Winhester')

# print(st1.name)
# print(st2.name)

# print(f'Before study {st1.name}: {st1.books}, {st1.language}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_work}')

# st1.read_book('grokman alghoritmy')
# st1.read_book('Pyhton from beginer')
# st1.read_book('Algoritms')
# st1.read_book('Marimatiks')

# st1.do_project()
# st1.do_project()

# st1.learn_lang('Phyton', 60)
# st1.learn_lang('Phyton', 90)
# st1.learn_lang('JS', 90)

# st1.do_project()
# print(f'After study {st1.name}: {st1.books}, {st1.language}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_work}')

# -----------------------------------------------------

# class Car:
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model

#     def show_info(self):
#         return f'{self.brand} -> {self.model}'
    
#     def __str__(self) -> str:
#         return f'{self.brand} -> {self.model}'

# obj = Car('BMW', '8 series')
# print(obj)
# print(obj.show_info())

# ---------------------------------------------------------
# class Soda:
#     def __init__(self, ingredient=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def __str__(self) -> str:
#         return 'Normal one!' if not self.ingredient else f'Gazirovka iz {self.ingredient}'
    
# a = Soda(1231)
# b = Soda(True)
# print(a, b)

# energetic = Soda('Gorilla')
# limonad = Soda('Malina')
# print(energetic, limonad)

# ---------------------------------------------
# import random


# class Sniper:
#     health = 100

#     def __init__(self, name) -> None:
#         self.name = name

#     def __str__(self) -> str:
#         return self.name

#     def shoot(self, other):
#         other.health -= 20
#         print(f' Атаковал {self}')
#         print(f'y {other} осталось {other.health}')

# sniper1 = Sniper('Maikl')
# sniper2 = Sniper('Din Winchester')

# while sniper1.health and sniper2.health:
#     choice = random.randint(1, 2)
#     sniper1.shoot(sniper2) if choice == 1 else sniper2. shoot(sniper1)
#     print()

# print(f'{sniper1 if sniper1.health else sniper2} won the game!')
 
