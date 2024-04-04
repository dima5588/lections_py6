# принципы ООП:
# 1.Насиление 
# 2.Инкапсуляция
# 3.Полиморфизм

# 4.Абстракция
# 5.Композиции
# 6.Агрегация
# --------------------------
# Нсиление
# Пощзволяет принимать родительские методы и атрибуты дочкрнему классу

# Рдительский класс
# Дочкрный класс
# --------------------------

# class Animal:
#     def print_info(self):
#         print('I\'m an Animal!')
              

# class Lion(Animal):
#      pass
     
# lion = Lion()
# lion.print_info()
# print(dir(Lion))

# class Animal:
#     def say(self):
#         print(f'This animals name is {self.name}: {self.golos}')

#     def eat(self):
#         print(f'{self.name} eats: {self.meal}')

# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meal = 'meat'
#     griva = 'True'

#     def info(self):
#         print(f'{self.name} griva: {self.griva}')

# class Dog(Animal):
#     name = 'dog'
#     golos = 'bark'
#     meal = 'meat'


# class Koala(Animal):
#     name = 'koala'
#     golos = 'roar'
#     meal = 'efkalit'

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()
# print()
# simba.say()
# simba.eat()
# simba.info()
# print()
# julian.say()
# julian.eat()

# ------------------------
# class Person:
#     def info(self):
#         print('I\'m person from Bishkek')


# class Student(Person):
#     def info(self):
#         print('I\'m study at Manas Universute')
#         super().info()
# obj = Student()
# obj.info()

# class Latop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def get_info(self):
#         return {'brand': self.brand, 'model': self.model, 'price': self.price}
    
# class Acer(Latop):
#     def __init__(self, model, price, year, videcard):
#         super().__init__('Acer', model, price)
#         self.year = year
#         self.video = videcard

#     def get_info(self):
#         repr = super().get_info()
#         repr['yaer'] = self.year
#         repr['vidiocard'] = self.video
#         return repr
    
# class Apple(Latop):
#     def __init__(self, model, price, display, year):
#         super().__init__('Mackbook', model, price)
#         self.display = display
#         self.year = year

#     def get_info(self):
#         repr = super().get_info()
#         repr['year'] = self.year
#         repr['display'] = self.display
#         return repr
    
# mac = Apple('Pro', 1500, 14, 2020)
# print(mac.get_info())

# acer = Acer('swift', 600, 2019, 'Nvidia')
# print(acer.get_info())