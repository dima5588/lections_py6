
# Mxixns
# Миксины - классы которые использует для наследование и передачи дочерним классам определеных методовб но от них не создаются обекты
# для чего:
# 1 вы  хотите предоставить множество доп методов для классов
# 2 вы хотите использовать один конкретный метод во множустве разных классов

# class EngineMixin:
#     def start_engine(self):
#         print('started engine')

# class RadioMixin:
#     def play_radio(self):
#         print('miusic is playing')

# class Plane(EngineMixin):
#     pass

# class Car(EngineMixin, RadioMixin):
#     pass

# class Train(EngineMixin, RadioMixin):
#     pass

# class FlyMixin:
#     def fly(self):
#         print('I can fly!')

# class WalkMixin:
#     def walk(self):
#         print('I can walk!')

# class SwimMixin:
#     def swim(self):
#         print('I can swim!')


# class Human(WalkMixin, SwimMixin):
#     name = 'human'

#     def talk():
#         print('I can talk!')

# class Fish(SwimMixin):
#     name = 'fish'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'flying fish'

# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     name = 'duck'

# obj = Human()
# obj.walk()
# obj.swim()