# class Employee:
#     bonus = 1.5

#     def __init__(self, first_name, last_name, salary) -> None:
#         self.name = f'{first_name} {last_name}'
#         self.salary = salary
    
#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'
    
#     def increase(self):
#         self.salary *= self.bonus

#     def __str__(self) -> str:
#         return self.get_info()
    

# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs=[]):
#         super().__init__(first_name, last_name, salary)
#         self.devs.append(developer)



# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing')

#     def ride(self):
#         print('We\'re ridding on the ground!')

# class Plane:
#     def play_music_at_station(self):
#         print('Listening Ed Sheern')

#     def fly(self):
#         print('We\'re flying')

# class FutureAuto(Plane, Auto):
#     pass

# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()
# obj.play_music_at_station()
# ------------------------------------

