
# Задание: Работа с базой данных PostgreSQL

# Цели задания:

# Проверка знаний и умений по добавлению, обновлению и заполнению данными таблиц в базе данных PostgreSQL.

# Описание задания:                 

# В рамках данного задания вам предстоит работать с базой данных для интернет-магазина. Вам будет необходимо создать таблицы, добавить в них данные, обновить определенные записи и выполнить ряд запросов для проверки введенной информации.

# Часть 1: Подготовка базы данных

# 1. Создайте базу данных OnlineStore`.       
# CREATE DATABASE OnlineStore;

# 2. Внутри базы данных создайте следующие таблицы:

# Products (Товары): id (первичный ключ), пате (имя), price (цена), quantity (количество на складе).

# . Customers (Покупатели): id (первичный ключ), first_name (имя), last_name (фамилия), email (электронная почта).

# . Orders (Заказы): id (первичный ключ), customer_id (внешний ключ к таблице Customers), order_date (дата заказа), total_amount (общая сумма).

# CREATE TABLE Products (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(255),
#     price NUMERIC(10, 2),
#     quantity INTEGER
# );

# CREATE TABLE Customers (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(255),
#     last_name VARCHAR(255),
#     email VARCHAR(255)
# );

# CREATE TABLE Orders (
#     id SERIAL PRIMARY KEY,
#     customer_id INTEGER REFERENCES Customers(id),
#     order_date DATE,
#     total_amount NUMERIC(10, 2)
# );



# Часть 2: Заполнение таблиц данными

# 1. Добавьте не менее пяти записей в таблицу 'Products'.

# INSERT INTO Products (name, price, quantity) VALUES
# ('Product1', 10.99, 100),
# ('Product2', 24.99, 50),
# ('Product3', 5.99, 200),
# ('Product4', 15.49, 75),
# ('Product5', 8.99, 120);

# 2. Добавьте не менее трех записей в таблицу Customers.

# INSERT INTO Customers (first_name, last_name, email) VALUES
# ('John', 'Doe', 'john.doe@example.com'),
# ('Jane', 'Smith', 'jane.smith@example.com'),
# ('Alice', 'Johnson', 'alice.johnson@example.com');


# 3. Создайте заказы в таблице Orders, связав их с покупателями и укажите общую сумму заказа.

# INSERT INTO Orders (customer_id, order_date, total_amount) VALUES
# (1, '2024-03-11', 55.45),
# (2, '2024-03-11', 36.97),
# (3, '2024-03-11', 72.15);


# Часть 3: Обновление данных

# 1. Измените цены на некоторые товары в лице Products.
# UPDATE Products SET price = 12.99 WHERE name = 'Product1';
# UPDATE Products SET price = 29.99 WHERE name = 'Product2';

# 2. Обновите информацию о количестве товара на складе после создания заказов.

# UPDATE Products SET quantity = quantity - 10 WHERE name = 'Product1';
