"""
1. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
элементов начиналась с 1. Например:
x = MyList([1,2,3,4,5])
x[1] → 1
"""
# class MyList(list):
#     def __getitem__(self, index):
#         if isinstance(index, int):
#             index -= 1
#         return super().__getitem__(index)

#     def __setitem__(self, index, value):
#         if isinstance(index, int):
#             index -= 1
#         super().__setitem__(index, value)

# x = MyList([1, 2, 3, 4, 5])
# print(x[1])  
# x[1] = 10
# print(x[1]) 

"""
2. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
Также в методе new напишите условие для удаления
пробелов и пустых строк в созданных словах.
"""
# class Word:
#     def __init__(self, word):
#         self.word = word.strip()

#     def __gt__(self, other):
#         return len(self.word) > len(other.word)

#     def __lt__(self, other):
#         return len(self.word) < len(other.word)

#     def __ge__(self, other):
#         return len(self.word) >= len(other.word)

#     def __le__(self, other):
#         return len(self.word) <= len(other.word)

#     def __str__(self):
#         return self.word

# word1 = Word("hello")
# word2 = Word("world")
# word3 = Word("python")

# print(word1 > word2)  
# print(word2 >= word3) 
# print(word3 < word1) 
# print(word1 <= word3)

"""
3. Создайте класс BankAccount, представляющий банковский счет. Реализуйте магические методы init, str, add и sub, чтобы поддерживать инициализацию счета, вывод информации о счете и операции пополнения и снятия средств.
"""
# class BankAccount:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = balance

#     def __str__(self):
#         return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

#     def __add__(self, amount):
#         self.balance += amount
#         return self.balance

#     def __sub__(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         self.balance -= amount
#         return self.balance

# account = BankAccount("John")
# print(account)  
# account + 100  
# print(account)  
# account - 50
# print(account)  
