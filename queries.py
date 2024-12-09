import sqlite3

# Стратегія Lazy Loading (завантаження даних за потребою)
def get_orders_lazy(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders WHERE TotalAmount > 10")  # Завантажуємо замовлення
    orders = cursor.fetchall()
    for order in orders:
        # Для кожного замовлення окремо завантажуємо клієнта
        cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (order[1],))
        customer = cursor.fetchone()
        print(f"Order ID: {order[0]}, Customer: {customer[1]} {customer[2]}")

# Стратегія Eager Loading (завантажуємо всі дані за один запит)
def get_orders_eager(connection):
    cursor = connection.cursor()
    query = """
    SELECT Orders.OrderID, Orders.TotalAmount, Customers.Name 
    FROM Orders
    JOIN Customers ON Orders.CustomerID = Customers.CustomerID
    """
    cursor.execute(query)
    orders = cursor.fetchall()
    for order in orders:
        print(f"Order ID: {order[0]}, Customer: {order[2]}, Total Amount: {order[1]}")

# Стратегія Explicit Loading (завантажуємо дані по мірі потреби)
def get_orders_explicit(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders WHERE TotalAmount > 15")
    orders = cursor.fetchall()
    for order in orders:
        print(f"Order ID: {order[0]}, Total Amount: {order[3]}")
        # Після цього явно завантажуємо дані про клієнта
        cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (order[1],))
        customer = cursor.fetchone()
        print(f"Customer: {customer[1]} {customer[2]}")

# Агрегатна функція для підрахунку загальної кількості бонусних балів
def get_total_bonus_points(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(BonusPoints) FROM LoyaltyCards")
    result = cursor.fetchone()
    print(f"Загальна кількість бонусних балів: {result[0]}")

# Фільтрація замовлень за сумою
def get_high_value_orders(connection, min_amount):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders WHERE TotalAmount > ?", (min_amount,))
    rows = cursor.fetchall()
    print(f"\nЗамовлення з сумою більше {min_amount}:")
    for row in rows:
        print(row)

# Сортування замовлень за сумою
def get_sorted_orders(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Orders ORDER BY TotalAmount DESC")
    rows = cursor.fetchall()
    print("\nЗамовлення, відсортовані за сумою:")
    for row in rows:
        print(row)
