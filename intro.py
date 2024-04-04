# OOP - обектно-орентированое програмирование

# Класс - это описание того, как должен выглядить обьект то есть в классе мы описоваем какими свойствами(данными) и поведением(функциями) должен обладать обект

# обьект - это сушность которую мы создаем от классаб у обьекта есть собственное состояние свойств(данные)

# методы - функции внутри класса
#-------------------------------------------------------------

# class Human:
#     age = 25

#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + '' + last_name
#         self.job = job
#         self.citizen = citizenship
        
#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, Job: {self.job}, Citizen: {self.citizen}'
    

# john = Human('John', 'Snow', 'King', 'Norther')
# anvar = Human('Anvar', 'Lansitere', 'Programmer', 'KR')

# # print(john)
# # print(type(john))
# # print(dir(john))
# print(john.show_info())
# print(anvar.show_info())
# john.age = 25
# john.job = 'King of Westeros'
# print(john.show_info)

# -----------------------------------------------------
# class Dog:
#     # аттрибуты класса
#     age = 0
#     ushi = True

#     def __init__(self, name, color):
#         "Иницифлизатор, именно здесь создаются аттрибуты обькета"
#         # self - сыллка на обект который создвются
#         self.name = name
#         self.color = color

#     def bark(self):
#         print(f'{self.name}лает!')

#     def show_info(self):
#         print(f'Name: {self.name}, Age: {self.age}, color: {self.color}, ushi: {self.ushi}')

# rex = Dog('Rex', 'Black')
# pluot = Dog(name='Pluto', color='brown')
# aktosh = Dog('Aktosh', 'gray')

# rex.show_info()
# pluot.show_info()
# aktosh.show_info()

# rex.age = 2
# pluot.age = 7
# aktosh.age = 5
# aktosh.ushi = False

# rex.show_info()
# pluot.show_info()
# aktosh.show_info()
# ----------------------------------------------------
# class Human:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.galod = 100
        
#     def walk(self):
#         print(f'{self.name} walking arpund!')
#         self.galod += 30

#     def work(self):
#         print(f'{self.name} rabotu raboatet!')
#         self.galod += 50

#     def eat(self, meal, finish=True):
#         print(f'{self.name} покушала {meal}!')
#         self.galod -= 60 if finish else 30

#     def info(self):
#         print(f'{self.name} --> {self.galod}')

# obj = Human('Raychel')
# obj.info()
# obj.eat('kruasan')
# obj.eat('Shaurma', finish=False)
# obj.info()
# obj.walk()
# obj.work()
# obj.info()
# obj.eat('Burger')
# obj.eat('freand Potato', finish=False)
# obj.info()

