# Функція для заповнення бази даних початковими даними
def insert_initial_data(connection):
    cursor = connection.cursor()

    # Додавання 10 різних покупців до таблиці Customers
    cursor.executemany("INSERT INTO Customers (Name, Email, Phone) VALUES (?, ?, ?)", [
        ('John Doe', 'john.doe@example.com', '+123456789'),
        ('Jane Smith', 'jane.smith@example.com', '+987654321'),
        ('Michael Brown', 'michael.brown@example.com', '+112233445'),
        ('Sarah Johnson', 'sarah.johnson@example.com', '+223344556'),
        ('David Williams', 'david.williams@example.com', '+334455667'),
        ('Emily Davis', 'emily.davis@example.com', '+445566778'),
        ('James Wilson', 'james.wilson@example.com', '+556677889'),
        ('Olivia Taylor', 'olivia.taylor@example.com', '+667788990'),
        ('Daniel Lee', 'daniel.lee@example.com', '+778899001'),
        ('Sophia Harris', 'sophia.harris@example.com', '+889900112')
    ])

    # Додавання бонусних карток до таблиці LoyaltyCards
    cursor.executemany("INSERT INTO LoyaltyCards (CustomerID, BonusPoints, IssueDate) VALUES (?, ?, ?)", [
        (1, 100, '2024-01-15'),
        (2, 200, '2024-02-10'),
        (3, 150, '2024-03-01'),
        (4, 250, '2024-04-05'),
        (5, 300, '2024-05-10'),
        (6, 50, '2024-06-20'),
        (7, 75, '2024-07-15'),
        (8, 120, '2024-08-05'),
        (9, 90, '2024-09-10'),
        (10, 110, '2024-10-25')
    ])

    # Додавання товарів до таблиці Products
    cursor.executemany("INSERT INTO Products (ProductName, Price) VALUES (?, ?)", [
        ('Milk', 1.99),
        ('Bread', 0.99),
        ('Eggs', 2.49),
        ('Cheese', 3.59),
        ('Butter', 2.29),
        ('Yogurt', 1.49),
        ('Cereal', 2.99),
        ('Apple', 1.19),
        ('Orange', 1.29),
        ('Carrot', 0.89)
    ])

    # Додавання замовлень до таблиці Orders
    cursor.executemany("INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, BonusUsed) VALUES (?, ?, ?, ?)", [
        (1, '2024-03-05', 15.00, 10),
        (2, '2024-03-06', 20.00, 5),
        (3, '2024-03-07', 25.00, 15),
        (4, '2024-03-08', 30.00, 20),
        (5, '2024-03-09', 35.00, 25),
        (6, '2024-03-10', 40.00, 30),
        (7, '2024-03-11', 45.00, 35),
        (8, '2024-03-12', 50.00, 40),
        (9, '2024-03-13', 55.00, 45),
        (10, '2024-03-14', 60.00, 50)
    ])

    # Додавання транзакцій до таблиці Transactions
    cursor.executemany(
        "INSERT INTO Transactions (CardID, OrderID, TransactionDate, PointsEarned, PointsSpent) VALUES (?, ?, ?, ?, ?)",
        [
            (1, 1, '2024-03-05', 20, 10),
            (2, 2, '2024-03-06', 30, 5),
            (3, 3, '2024-03-07', 40, 15),
            (4, 4, '2024-03-08', 50, 20),
            (5, 5, '2024-03-09', 60, 25),
            (6, 6, '2024-03-10', 70, 30),
            (7, 7, '2024-03-11', 80, 35),
            (8, 8, '2024-03-12', 90, 40),
            (9, 9, '2024-03-13', 100, 45),
            (10, 10, '2024-03-14', 110, 50)
        ])

    connection.commit()  # Зберігаємо зміни в базі даних

