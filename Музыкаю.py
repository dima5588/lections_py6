
# Написать платформу для прослушивания музыки
# 1) Класс Пользователь с юзернеймом, возраст, эл. почтой и подпиской(по дефолту - Без подписки, если подписка не оформлена, то с каждым прослушиванием появялется реклама, спам), плейлист(по дефолту - пустой список). Можно дополнительно еще пароль сделать, с валидацией, вся информация должна быть приватной.
# Нужно провалидировать все данные(почту на наличие @, пароль, возраст)

# - Метод для оформления подписки, для добавления в пейлист песни, 
# - метод для прослушивания песни, 
# - метод который прослушивает весь плейлист по очередно

# 2) Класс жанр в названием

# 3) Класс музыка с названием, автором, жанром, длительностью      

# 4) Класс работник, который наследуется от Пользователя, но у него есть доп атрибут - роль (например админ), и платформа где он работает

# 5) Класс платформа для прослушивания музыки, например - Spotify, у которого должны быть списки песен, жанры, список пользователей с полпиской и без

# - методы для  просмотра всех песен,
# - методы для просмотра песен по определенному жанру,
# - метод для оформления подписки у пользователя, если
# - метод для поиска песни по названию
# - метод для добавления определенной песни в плейлист пользователя
# - метод удаления, добавления песни, жанра из списка Платформы, которую может сделать только админ этой платформы
# - метод блокировки, удаления пользователя, если это потребуется
# import re

# class User:
#     def __init__(self, username, age, email, subscription="Без подписки", password=None):
#         self.__username = username
#         self.__age = self.__validate_age(age)
#         self.__email = self.__validate_email(email)
#         self.__subscription = subscription
#         self.__password = password
#         self.__playlist = []

#     def __validate_age(self, age):
#         if not isinstance(age, int) or age < 0:
#             raise ValueError("Возраст должен быть положительным числом")
#         return age

#     def __validate_email(self, email):
#         if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
#             raise ValueError("Некорректный адрес электронной почты")
#         return email

#     def set_password(self, password):
#         self.__password = password

#     def get_username(self):
#         return self.__username

#     def get_age(self):
#         return self.__age
    
#     def get_email(self):
#         return self.__email

#     def get_subscription(self):
#         return self.__subscription

#     def get_playlist(self):
#         return self.__playlist

#     def subscribe(self):
#         self.__subscription = "Подписка оформлена"

#     def add_to_playlist(self, song):
#         self.__playlist.append(song)

#     def listen_playlist(self):
#         for song in self.__playlist:
#             print(f"Сейчас играет: {song}")

# user1 = User("user1", 25, "user1@example.com")
# user1.add_to_playlist("Песня 1")
# user1.add_to_playlist("Песня 2")
# user1.subscribe()
# user1.listen_playlist()


# class Genre:
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):
#         return self.__name

# genre1 = Genre("Rock")
# print(genre1.get_name())

# class Song:
#     def __init__(self, title, author, genre, duration):
#         self.__title = title
#         self.__author = author
#         self.__genre = genre
#         self.__duration = duration

#     def get_title(self):
#         return self.__title

#     def get_author(self):
#         return self.__author

#     def get_genre(self):
#         return self.__genre

#     def get_duration(self):
#         return self.__duration

# song1 = Song("Моргенштерн 1", "Кадиллак 1", genre1, 180)
# print(song1.get_title(), song1.get_author(), song1.get_genre().get_name(), song1.get_duration())


# class Employee(User):
#     def __init__(self, username, age, email, role, platform):
#         super().__init__(username, age, email)
#         self.__role = role
#         self.__platform = platform

#     def get_role(self):
#         return self.__role

#     def get_platform(self):
#         return self.__platform

# employee1 = Employee("employee1", 30, "employee1@example.com", "Моргенштерн", "Spotify")
# print(employee1.get_username(), employee1.get_role(), employee1.get_platform())

