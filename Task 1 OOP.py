
# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .

# class Car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color

#     def get_auto(self):
#         return f"Марка: {self.brand}, Год выпуска: {self.year}, Цвет: {self.color}"

#     def get_year(self):
#         current_year = 2024  
#         age = current_year - self.year
#         return f"Автомобилю {self.brand} {self.year} года выпуска, {age} года"


# my_car = Car("Toyota", 2010, "синий")
# print(my_car.get_auto())  
# print(my_car.get_year())  


# Добавьте атрибут horsepower, который равен 85. 

# class Car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.horsepower = 85

#     def get_auto(self):
#         return f"Марка: {self.brand}, Год выпуска: {self.year}, Цвет: {self.color}, Мощность: {self.horsepower} л.с."

#     def get_year(self):
#         current_year = 2024
#         age = current_year - self.year
#         return f"Автомобилю {self.brand} {self.year} года выпуска, исполнилось {age} лет."


# my_car = Car("Toyota", 2010, "серебристый")
# print(my_car.get_auto())
# print(my_car.get_year())


# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

# class Car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.horsepower = 85

#     def get_auto(self):
#         return f"Марка: {self.brand}, Год выпуска: {self.year}, Цвет: {self.color}, Мощность: {self.horsepower} л.с."

#     def get_year(self):
#         current_year = 2024 
#         age = current_year - self.year
#         return f"Автомобилю {self.brand} {self.year} года выпуска, исполнилось {age} лет."

#     def add_horsepower(self):
#         if self.brand in ["Mers", "Bmw", "Poshe"]:
#             self.horsepower += 40
#         else:
#             self.horsepower += 20


# my_car = Car("Toyota", 2010, "серебристый")
# print("До увеличения мощности:", my_car.get_auto())
# my_car.add_horsepower()
# print("После увеличения мощности:", my_car.get_auto())

# mers_car = Car("Mers", 2015, "черный")
# print("До увеличения мощности:", mers_car.get_auto())
# mers_car.add_horsepower()
# print("После увеличения мощности:", mers_car.get_auto())


#  Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

# bmw = Car("BMW", 2020, "черный")

# print("Марка автомобиля:", bmw.brand)
# print("Год выпуска автомобиля:", bmw.year)
# print("Цвет автомобиля:", bmw.color)

# print("\nИнформация об автомобиле:")
# print(bmw.get_auto())

# print("\nВозраст автомобиля:")
# print(bmw.get_year())

# print("\nУвеличение мощности:")
# bmw.add_horsepower()
# print(bmw.get_auto())

#  Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto

# car1 = Car("Toyota", 2015, "серебристый")
# car2 = Car("Honda", 2022, "красный")

# print("Информация об автомобиле 1:")
# print(car1.get_auto())

# print("\nИнформация об автомобиле 2:")
# print(car2.get_auto())


#  Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course

#     def get_student(self):
#         return f"Студент: {self.name}, Возраст: {self.age}, Курс: {self.course}"

#     def get_birth_year(self):
#         current_year = 2024  
#         birth_year = current_year - self.age
#         return f"{self.name} родился в {birth_year} году."


# student1 = Student("Иван", 20, 3)
# print(student1.get_student())
# print(student1.get_birth_year())

# student2 = Student("Мария", 22, 4)
# print(student2.get_student())
# print(student2.get_birth_year())



# # Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента.

# # Создание нескольких экземпляров класса Student
# student1 = Student("Иван", 20, 3)
# student2 = Student("Мария", 22, 4)
# student3 = Student("Алексей", 21, 2)

# print("Студент 1:")
# print(student1.get_student())
# print(student1.get_birth_year())

# print("\nСтудент 2:")
# print(student2.get_student())
# print(student2.get_birth_year())

# print("\nСтудент 3:")
# print(student3.get_student())
# print(student3.get_birth_year())



