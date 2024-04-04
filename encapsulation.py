# Инкапсуляция:
# 2. Механизм сокрытия при помощи которого можно ограничить доступ одного компонента программы к другому
# 1. Я -зыковая констркукцияб которая помогает связать данныу с методами для их обработки и управления (связь между данными и методами котрые управляют им)

# class Phone:
#     number = '+996777777777'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')
#         print(f'Мой номер: {Phone.number}')

# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как механизм сокрытия 
# 3 уровня сокрытия данных в питоне
#             1. Публичный(public) - number, print_number
#             2. Защищенные(_protected) - _number
#             3. Приватный(__private) - __number

# class Car:
#     _country = 'Germany'
#     _motor = 'GTR'

#     def __init__(self) -> None:
#         self.marka = 'BMW'
#         self._model = 'I8'
#         self.__color = 'black'

# obj = Car()
# print(obj.marka)
# print(obj._country, obj._model)

# class Phone:
#     username = 'Mikl'
#     _caller = 'Jame'
#     __count_of_class = 17

#     def call(self):
#         print(f'{self._caller} звонит вам!')
#         question = input('Взять трубку(yes\no)')
#         if question.lower().strip() == 'yes':
#             self.__turn_on()
#         else:
#             print('сбросили трубку!')

#     def __turn_on(self):
#         self.__incremant_class()

# class Person:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f'My name is {self.name} and I\'m {self.age} years old!')

# obj = Person('John', 18)
# obj.display_info()   
# obj.name = [1, 2, 3, 4]
# obj.age  =-25
# obj.display_info()

# -------------------------------------------------------

# getter & setter
# они нужны чтобы избежать прямого обрашения к сокрытым атрибутам
# при этом можно добавить логику владация(проверки)
# данных которые
