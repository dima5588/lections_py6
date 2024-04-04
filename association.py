# Ассоция - принцип ООП в котором два класса связаны друг с другом
# агрегация - слабая связь
# комозиция - слиьная связь

# class Batary:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battary = Batary()

# a = Iphone('write')
# print(a.battary._power)
# a.battary._power -=50
# print(a.battary._power)
# a.battary.charge()
# print(a.battary._power)

# class Nokia:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.battery = battery

# battery = Batary()
# nokia1 = Nokia('gray', battery)
# del nokia1

# nokia2 = Nokia('black', battery)      