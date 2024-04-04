"""
1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""
# class Circle:
#      color = 'blue'
#      pi = 3.14

#      def __init__(self, radius):
#          self.radius = radius

#      def area(self):
#          return self.pi * self.radius ** 2
    
# circle_instance = Circle(5)
# circle_instance.color = 'red'
# area = circle_instance.area()

# print(f"Площадь круга с радиусом {circle_instance.radius} и цветом {circle_instance.color} равна {area}")

"""
2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.
"""
# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#         return f"Название песни: {self.title}"

#     def show_author(self):
#         return f"Автор песни: {self.author}"

#     def show_year(self):
#         return f"Песня вышла в {self.year} году"

# my_favorite_song = Song("Cadilck", "Morgenshern", 2020)

# print(my_favorite_song.show_title())
# print(my_favorite_song.show_author())
# print(my_favorite_song.show_year())

"""
3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""
# class Taxi:
#     def __init__(self, company_name, start_price, price_per_km):
#         self.company_name = company_name
#         self.start_price = start_price
#         self.price_per_km = price_per_km

#     def calculate_price(self, distance):
#         total_price = self.start_price + distance * self.price_per_km
#         return total_price

# namba_taxi = Taxi("Namba", 200, 50)
# yandex_taxi = Taxi("Yandex", 150, 45)
# jorgo_taxi = Taxi("Jorgo", 180, 55)

# distance = 10 
# print(f"Стоимость поездки в компании {namba_taxi.company_name}: {namba_taxi.calculate_price(distance)} сом")
# print(f"Стоимость поездки в компании {yandex_taxi.company_name}: {yandex_taxi.calculate_price(distance)} сом")
# print(f"Стоимость поездки в компании {jorgo_taxi.company_name}: {jorgo_taxi.calculate_price(distance)} сом")

"""
4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""
# class PhoneBook:
#     def __init__(self):
#         self.contacts = []

#     def add_contact(self, first_name, last_name, phone_number):
#         contact = {
#             'first_name': first_name,
#             'last_name': last_name,
#             'phone_number': phone_number
#         }
#         self.contacts.append(contact)

#     def get_info(self):
#         for contact in self.contacts:
#             full_name = f"{contact['first_name']} {contact['last_name']}"
#             print(f"Контакт: {full_name}, телефон: {contact['phone_number']}")


# phone_book = PhoneBook()

# phone_book.add_contact("Иван", "Петров", "+996555777888")
# phone_book.add_contact("Мария", "Иванова", "+996777888999")
# phone_book.add_contact("Алексей", "Сидоров", "+996999888777")

# phone_book.get_info()

"""
5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.
"""
# class Salary:
#     tax_rate = 0.08  # 8% налог

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def calculate_tax_paid(self):
#         total_tax_paid = self.salary * self.tax_rate * self.experience
#         return total_tax_paid

# salary_instance = Salary(50000, 5)  

# total_tax_paid = salary_instance.calculate_tax_paid()
# print(f"Сумма налога, заплаченного за весь стаж работы: {total_tax_paid} сом")
