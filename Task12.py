
# Задача 1: "Dollar"

#     Цель: Создать функцию dollarize, преобразующую числа в долларовый формат, и класс MoneyFmt для управления денежными суммами.
#     Описание:
#         Функция dollarize должна принимать дробное число и возвращать строку, представляющую сумму в долларовом формате.
#         Класс MoneyFmt использует внутренний атрибут amount для хранения денежной суммы и предоставляет методы для обновления суммы, возвращения ее как строки в долларовом формате и как исходного числового значения.
#         Пример использования:
#         # cash = MoneyFmt(12345678.021) 
#         # print(cash) -- выводит "$12,345,678.02" 
#         # cash.update(100000.4567) 
#         # print(cash) -- выводит "$100,000.46" 
#         # cash.update(-0.3) 
#         # print(cash) -- выводит "-$0.30" 
#         # repr(cash) -- выводит -0.3 
# def dollarize(amount):
#     return "${:,.2f}".format(amount)

# class MoneyFmt:
#     def __init__(self, amount):
#         self.amount = amount

#     def update(self, amount):
#         self.amount = amount

#     def __str__(self):
#         return "${:,.2f}".format(self.amount)

#     def __repr__(self):
#         return str(self.amount)

# cash = MoneyFmt(12345678.021)
# print(cash)
# cash.update(100000.4567)
# print(cash)  
# cash.update(-0.3)
# print(cash)  
# print(repr(cash))



# Задача 2: "Велосипед"

#     Цель: Реализовать класс Bike, моделирующий велосипед с различными атрибутами и методами управления.
#     Описание:
#         Класс должен содержать атрибуты для стоимости, производителя, модели, года выпуска, состояния, цены продажи и статуса продажи.
#         Методы должны позволять устанавливать цену продажи, учитывая минимальную прибыль, обслуживать велосипед, изменяя его состояние и стоимость ремонта, и продавать велосипед, изменяя его статус и рассчитывая прибыль.

# class Bike:
#     def __init__(self, cost, manufacturer, model, year, condition, sale_price=None, sale_status="Not for sale"):
#         self.cost = cost
#         self.manufacturer = manufacturer
#         self.model = model
#         self.year = year
#         self.condition = condition
#         self.repair_cost = 0
#         self.sale_price = sale_price
#         self.sale_status = sale_status

#     def set_sale_price(self, price, min_profit=50):
#         if price >= self.cost + min_profit:
#             self.sale_price = price
#             return True
#         return False

#     def repair(self, cost):
#         self.repair_cost += cost
#         self.condition = "Repaired"
#         self.sale_status = "Not for sale"
#         return True

#     def sell(self):
#         if self.sale_price is not None:
#             profit = self.sale_price - self.cost - self.repair_cost
#             self.sale_status = "Sold"
#             return profit
#         return None

# bike = Bike(200, "Manufacturer", "Model", 2022, "Good")
# print(bike.condition)  
# bike.repair(50)
# print(bike.condition)  
# print(bike.sell()) 
# bike.set_sale_price(300)
# print(bike.sell())  
# print(bike.sale_status)


# Задача 3: "Герой"

#     Цель: Разработать программу, имитирующую взаимодействие между солдатами и героями в контексте игры-стратегии.
#     Описание:
#         Необходимо создать классы для солдат и героев, каждый с уникальным номером и принадлежностью к команде.
#         Солдаты могут "следовать" за героями своей команды, а герои могут повышать свой уровень.
#         В программе должны генерироваться солдаты для двух команд, после чего сравнивается количество солдат в каждой команде, и у героя команды с большим числом солдат повышается уровень.

# import random

# class Soldier:
#     def __init__(self, number, team):
#         self.number = number
#         self.team = team
#         self.following_hero = None

#     def follow_hero(self, hero):
#         self.following_hero = hero

#     def __str__(self):
#         return f"Soldier {self.number} of Team {self.team}"

# class Hero:
#     def __init__(self, number, team):
#         self.number = number
#         self.team = team
#         self.level = 1

#     def increase_level(self):
#         self.level += 1

#     def __str__(self):
#         return f"Hero {self.number} of Team {self.team} (Level {self.level})"

# class Team:
#     def __init__(self, team_number, num_soldiers, num_heroes):
#         self.team_number = team_number
#         self.soldiers = [Soldier(i, team_number) for i in range(1, num_soldiers+1)]
#         self.heroes = [Hero(i, team_number) for i in range(1, num_heroes+1)]

#     def get_num_soldiers(self):
#         return len(self.soldiers)

#     def get_num_heroes(self):
#         return len(self.heroes)

#     def get_hero_with_most_soldiers(self):
#         return max(self.heroes, key=lambda hero: len([soldier for soldier in self.soldiers if soldier.following_hero == hero]))

#     def __str__(self):
#         return f"Team {self.team_number}: Soldiers - {len(self.soldiers)}, Heroes - {len(self.heroes)}"

# team1 = Team(1, 5, 1)
# team2 = Team(2, 3, 2)

# print(team1)
# print(team2)

# if team1.get_num_soldiers() > team2.get_num_soldiers():
#     hero = team1.get_hero_with_most_soldiers()
#     hero.increase_level()
#     print(f"Hero {hero.number} of Team {hero.team} has increased to level {hero.level}")
# else:
#     hero = team2.get_hero_with_most_soldiers()
#     hero.increase_level()
#     print(f"Hero {hero.number} of Team {hero.team} has increased to level {hero.level}")
