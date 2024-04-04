
#     Напишите класс Subscriber, у которого есть переменные экземпляра:
#         firstname
#         lastname
#         Сделайте так, чтобы метод __repr__ возвращал firstname + lastname

# class Subscriber:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def __repr__(self):
#         return f"{self.firstname} {self.lastname}"

# subscriber = Subscriber("John", "Doe")
# print(subscriber)           


    # Напишите класс Provider, у которого есть:
    #     переменный экземпляра name -- название провайдера
    #     переменный экземпляра subscribers -- список, в котором будут храниться экземпляры класса Subscriber
    #     переменный экземпляра payments -- словарь, ключём которого является экземпляр класса Subscriber, значением является сумма (вещественное число)
    #     метод register_payment, который принимает экземпляр класса Subscriber, и сумму, затем проверяет, есть ли такой экземпляр Subscriber в списке subscribers. 
    #         Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве значения
    #         Если нет, выкидывает (raise) ошибку ValueError

# class Provider:
#     def __init__(self, name):             
#         self.name = name
#         self.subscribers = []
#         self.payments = {}

#     def register_payment(self, subscriber, amount):
#         if subscriber in self.subscribers:
#             self.payments[subscriber] = amount
#         else:
#             raise ValueError("Экземпляр Subscriber не найден в списке подписчиков.")

# class Subscriber:
#     def __init__(self, name):
#         self.name = name

# provider = Provider("Provider1")
# subscriber1 = Subscriber("Subscriber1")
# subscriber2 = Subscriber("Subscriber2")

# provider.subscribers.append(subscriber1)

# try:
#     provider.register_payment(subscriber1, 100)
#     print(provider.payments)
# except ValueError as e:
#     print(e)

# try:
#     provider.register_payment(subscriber2, 200)
#     print(provider.payments)
# except ValueError as e:
#     print(e)


    # Напишите класс Terminal, у которого есть
    #     переменная экземпляра amount = 0
    #     переменная экземпляра providers = [ ]
    #     Регистрировать провайдера через метод register, который принимает экземпляр класса Provider и добавляет в providers
    #     Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider, экземпляр класса Subscriber и сумму (вещественное число). Внутри метода должен вызываться метод register_payment экземпляра класса Provider. register_payment успешно сработал, то в переменую amount нужно добавить сумму.

# class Terminal:
#     def __init__(self):
#         self.amount = 0
#         self.providers = []

#     def register(self, provider):
#         self.providers.append(provider)

#     def pay(self, provider, subscriber, amount):
#         if provider in self.providers:
#             if provider.register_payment(subscriber, amount):
#                 self.amount += amount
#                 return f"Платеж успешно принят от {subscriber.name} в размере {amount}"
#             else:
#                 return "Ошибка при выполнении платежа"
#         else:
#             return "Провайдер не зарегистрирован в терминале"

# class Provider:
#     def __init__(self, name):
#         self.name = name

#     def register_payment(self, subscriber, amount):
#         return True

# class Subscriber:
#     def __init__(self, name):
#         self.name = name


# terminal = Terminal()
# provider1 = Provider("Provider1")
# provider2 = Provider("Provider2")
# subscriber = Subscriber("Subscriber1")

# terminal.register(provider1)
# terminal.register(provider2)

# print(terminal.pay(provider1, subscriber, 100))
# print(terminal.amount)
