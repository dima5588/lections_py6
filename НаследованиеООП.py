

"""1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
"""
# class Auto:
#     def ride(self):
#         print("Riding on a ground")

# class Boat:
#     def swim(self):
#         print("Floating on water")

# class Amphibian(Auto, Boat):
#     pass

# amphibian = Amphibian()

# amphibian.ride()
# amphibian.swim()

"""2) Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""
# class RadioMixin:
#     def play_music(self, song_name):
#         print(f"Playing {song_name}")

# class Auto:
#     def ride(self):
#         print("Riding on a ground")

# class Boat:
#     def swim(self):
#         print("Floating on water")

# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# amphibian = Amphibian()

# amphibian.ride()
# amphibian.swim()
# amphibian.play_music("Despacito")

"""3) Будильник
Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
нему метод для установки будильника, при вызове которого должен включатся будильник."""
# class Clock:
#     def show_time(self):
#         print("Current time is 12:00")

# class Alarm:
#     def __init__(self):
#         self.is_alarm_on = False

#     def turn_on_alarm(self):
#         self.is_alarm_on = True
#         print("Alarm is now on")

#     def turn_off_alarm(self):
#         self.is_alarm_on = False
#         print("Alarm is now off")

# class AlarmClock(Clock, Alarm):
#     def set_alarm(self, alarm_time):
#         self.turn_on_alarm()
#         print(f"Alarm is set for {alarm_time}")

# alarm_clock = AlarmClock()

# alarm_clock.show_time()
# alarm_clock.set_alarm("7:00")
# alarm_clock.turn_off_alarm()

"""4) Разработчики
Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
get_info и coding.
Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
Так же бывают FullStack разработчики и
поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""
# from abc import ABC, abstractmethod

# class Coder(ABC):
#     experience = 0
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#        pass

#     @abstractmethod
#     def coding(self, hours):
#         pass

# class Backend(Coder):
#     def __init__(self, languages_backend):
#         self.languages_backend = languages_backend

#     def get_info(self):
#         return f"Backend developer with {self.experience} years of experience, knows {', '.join(self.languages_backend)}"

#     def coding(self, hours):
#         self.count_code_time += hours
#         return f"Coding for {hours} hours"

# class Frontend(Coder):
#     def __init__(self, languages_frontend):
#         self.languages_frontend = languages_frontend

#     def get_info(self):
#         return f"Frontend developer with {self.experience} years of experience, knows {', '.join(self.languages_frontend)}"

#     def coding(self, hours):
#         self.count_code_time += hours
#         return f"Coding for {hours} hours"

# class FullStack(Backend, Frontend):
#     def __init__(self, languages_backend, languages_frontend):
#         Backend.__init__(self, languages_backend)
#         Frontend.__init__(self, languages_frontend)

#     def get_info(self):
#         return f"FullStack developer with {self.experience} years of experience, knows {', '.join(self.languages_backend)} and {', '.join(self.languages_frontend)}"

#     def coding(self, hours):
#         self.count_code_time += hours
#         return f"Coding for {hours} hours"

# backend_dev = Backend(["Python", "Java"])
# frontend_dev = Frontend(["HTML", "CSS", "JavaScript"])
# fullstack_dev = FullStack(["Python", "Java"], ["HTML", "CSS", "JavaScript"])

# print(backend_dev.get_info())
# print(backend_dev.coding(5))
# print(f"Total coding time: {backend_dev.count_code_time} hours")

# print(frontend_dev.get_info())
# print(frontend_dev.coding(3))
# print(f"Total coding time: {frontend_dev.count_code_time} hours")

# print(fullstack_dev.get_info())
# print(fullstack_dev.coding(8))
# print(f"Total coding time: {fullstack_dev.count_code_time} hours")
