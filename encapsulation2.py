# Анотация свойств (@property(getter setter))

# class Person:
#     __name = 'john'
#     __age = 22

#     @property
#     def name(self):
#         "The name property(getter)"
#         print(self.__name)

#     @name.setter
#     def name(self, value):
#      if not isinstance(value, str): 
#         print('Invalid value for name!')
#      else:
#         print(f'Setter, {value}')
#         self.__name = value

#     @property
#     def age(self):
#        print(self.__age)

       
#     @age.setter
#     def name(self, value):
#      if not isinstance(value, str): 
#         print('Invalid value for name!')
#      else:
#         print(f'Setter, {value}')
#         self.__age = value


# obj = Person()
# obj.name
# obj.name = 'Din Winchester'
# obj.name
# obj.name = None
# obj.name
# obj.age
# obj.age = 30
# obj.age
# obj.age = -12
# obj.age = 208
# obj.age = 'qwqeq'
# obj.age

# -------------------------------------------------

# class Circle:
#     def __init__(self, radius) -> None:
#         self._radius = radius

#     def _get_radius(self):
#         print('getter, _get_radius')
#         return self._radius
    
#     def _set_radius(self, value):
#         print('stter, _set_radius')
#         if not isinstance(value, (int, float)):
#             print('radius must be an unt or float object')
#         else:
#             self._radius = value

#     radius = property(fget=_get_radius, fset=_set_radius)

# obj = Circle(5)
# print(obj.radius)
# obj.radius = 7.5
# print(obj.radius)

# class CoordinataerWriteError(Exception):
#     pass

# class Point:
#     def __init__(self, x, y) -> None:
#         self.__x = x
#         self.__y = y

#     @property
#     def x(self):
#         print(self.__x)

#     @property
#     def y(self):
#         print(self.__y)

#     @property
#     def y(self, value):
