# magic methods (магические методы)
# dunder methods (double underscore) -> __init__
# служебные методы


# Магия(фишка) заключается в том что эти методы запускается без прямого обращение к ним определенные методы могут отвечать за определенные операторы

# Магические методы сравнение
# __eq__(self, other) -> 5 == 8

# print('15' > 'ABC')

# class Word(str):
#     def __new__(cls, obj):
#         obj = obj.replace(' ', '')
#         return super().__new__(cls, obj)
    
#     def __init__(self, obj) -> None:
#         super().__init__()
#         self.obj = obj

#     def __gt__(self, other):
#         print('gt worked')
#         print(self, '---', other)
#         print(cls, '!!!!')
#         number = abs(args[0])
#         instace = super().__new__(cls)
#         instace.number = number
#         return instace
    
#     def __add__(self, other):
#         print('add worked')
#         res = self.number + other.number
#         print(f'Rsult: {self.number} + {other.number} = {res}')
#         return res
    
# value1 = Cifra(-117)
# value2 = Cifra(53)
# res = value1 + value2
# print(res)
#         if len(self) < len(other):
#             return self
#         elif len(self) < len(other):
#             return other
#         else:
#             return 'eq'
        
#     def __lt__(self, other) -> bool:
#         return len(self) < len(other)
    

#     def __eq__(self, other) -> bool:
#         return len(self) < len(other)

# obj = Word('      Hello Jphn    ')
# obj2 = Word(' Cod i   fy')

# print(obj > obj2)
# print(obj < obj2)
# ------------------------------------------

# class Cifra:
#     def __new__(cls, *args):
#         print(cls, '!!!!')
#         number = abs(args[0])
#         instace = super().__new__(cls)
#         instace.number = number
#         return instace
    
#     def __add__(self, other):
#         print('add worked')
#         res = self.number + other.number
#         print(f'Rsult: {self.number} + {other.number} = {res}')
#         return res
    
# value1 = Cifra(-117)
# value2 = Cifra(53)
# res = value1 + value2
# print(res)


# from  random import choice

# class Dog:
#     def sound(self):
#         print('Bark!')

# class Cat:
#     def sound(self):
#         print('Meow meow')

# class Horse:
#     def sound(self):
#         print('Igo-igo-go')

# class Pet:
#     def __new__(cls):
#         pet = choice([Dog, Cat, Horse])
#         self = super().__new__(pet)
#         print(f'I\'m{type(self).__name__}')
#         return self
    
#     def __init__(self) -> None:
#         print('Pet never was called')

# pet = Pet()
# pet.sound()
# --------------------------------------------
# SINGLETON

# class Singleton:
#     _intance = None

#     def __new__(cls):
#         if not cls._intance:
#             cls._intance = super().__new__(cls)
#             return cls._intance
        
#     def __str__(self) -> str:
#         return str(id(self))         
    
# a = Singleton()
# b = Singleton()
# print(a, b)
# print(a is b)
# obj = Singleton()
# obj1 = Singleton()
# print(obj, obj1)

# ----------------------------------------

# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)
    
#     def __getitem__(self, index):
#         return self.coins[index - 1]
    

# obj = Kopilka()
# print(obj.coins)
# print(obj.total)  

