import sqlite3

# Функція для створення підключення до бази даних
def create_connection():
    connection = sqlite3.connect('loyalty_system.db')
    return connection

# Функція для створення таблиць у базі даних
def create_tables(connection):
    cursor = connection.cursor()

    # Створення таблиці клієнтів
    cursor.execute("""CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT,
        Email TEXT,
        Phone TEXT
    )""")

    # Створення таблиці бонусних карток
    cursor.execute("""CREATE TABLE IF NOT EXISTS LoyaltyCards (
        CardID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER,
        BonusPoints INTEGER DEFAULT 0,
        IssueDate DATE,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    )""")

    # Створення таблиці товарів
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT,
        Price REAL
    )""")

    # Створення таблиці замовлень
    cursor.execute("""CREATE TABLE IF NOT EXISTS Orders (
        OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
        CustomerID INTEGER,
        OrderDate DATE,
        TotalAmount REAL,
        BonusUsed INTEGER,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    )""")

    # Створення таблиці транзакцій
    cursor.execute("""CREATE TABLE IF NOT EXISTS Transactions (
        TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
        CardID INTEGER,
        OrderID INTEGER,
        TransactionDate DATE,
        PointsEarned INTEGER,
        PointsSpent INTEGER,
        FOREIGN KEY (CardID) REFERENCES LoyaltyCards(CardID),
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    )""")

    connection.commit()

# Функція для заповнення бази даних тестовими даними
def insert_initial_data(connection):
    cursor = connection.cursor()

    # Додавання клієнтів
    cursor.executemany("INSERT INTO Customers (Name, Email, Phone) VALUES (?, ?, ?)", [
        ('John Doe', 'john@example.com', '+123456789'),
        ('Jane Smith', 'jane@example.com', '+987654321'),
        ('Alice Johnson', 'alice.johnson@example.com', '+1122334455'),
        ('Bob Brown', 'bob.brown@example.com', '+6677889900'),
        ('Charlie Davis', 'charlie.davis@example.com', '+5556667777'),
        ('David White', 'david.white@example.com', '+7778889999'),
        ('Eva Green', 'eva.green@example.com', '+8889990000'),
        ('Frank King', 'frank.king@example.com', '+4445556666'),
        ('Grace Lee', 'grace.lee@example.com', '+3334445555'),
        ('Helen Walker', 'helen.walker@example.com', '+2223334444')
    ])

    # Додавання бонусних карток
    cursor.executemany("INSERT INTO LoyaltyCards (CustomerID, BonusPoints, IssueDate) VALUES (?, ?, ?)", [
        (1, 100, '2024-01-15'),
        (2, 50, '2024-02-10'),
        (3, 150, '2024-03-01'),
        (4, 200, '2024-04-10'),
        (5, 75, '2024-05-10'),
        (6, 50, '2024-06-20'),
        (7, 300, '2024-07-15'),
        (8, 120, '2024-08-25'),
        (9, 80, '2024-09-10'),
        (10, 250, '2024-10-05')
    ])

    # Додавання товарів
    cursor.executemany("INSERT INTO Products (ProductName, Price) VALUES (?, ?)", [
        ('Milk', 1.99),
        ('Bread', 0.99),
        ('Eggs', 2.49),
        ('Butter', 3.49),
        ('Cheese', 5.99)
    ])

    # Додавання замовлень
    cursor.executemany("INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, BonusUsed) VALUES (?, ?, ?, ?)", [
        (1, '2024-03-05', 15.00, 10),
        (2, '2024-03-06', 20.00, 5),
        (3, '2024-03-07', 25.00, 15),
        (4, '2024-03-08', 30.00, 10),
        (5, '2024-03-09', 35.00, 5),
        (6, '2024-03-10', 40.00, 20),
        (7, '2024-03-11', 45.00, 10),
        (8, '2024-03-12', 50.00, 30),
        (9, '2024-03-13', 55.00, 25),
        (10, '2024-03-14', 60.00, 40)
    ])

    # Додавання транзакцій
    cursor.executemany("INSERT INTO Transactions (CardID, OrderID, TransactionDate, PointsEarned, PointsSpent) VALUES (?, ?, ?, ?, ?)", [
        (1, 1, '2024-03-05', 20, 10),
        (2, 2, '2024-03-06', 30, 5),
        (3, 3, '2024-03-07', 40, 15),
        (4, 4, '2024-03-08', 50, 10),
        (5, 5, '2024-03-09', 60, 5),
        (6, 6, '2024-03-10', 70, 20),
        (7, 7, '2024-03-11', 80, 10),
        (8, 8, '2024-03-12', 90, 30),
        (9, 9, '2024-03-13', 100, 25),
        (10, 10, '2024-03-14', 110, 40)
    ])

    connection.commit()

