# 4.1: Lazy Loading
def get_customer_with_loyalty_card_lazy(connection, customer_id):
    cursor = connection.cursor()

    # Завантаження клієнта
    cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
    customer = cursor.fetchone()

    if customer:
        print(f"Клієнт: {customer}")

        # Lazy loading: Завантажуємо LoyaltyCard лише коли потрібно
        cursor.execute("SELECT * FROM LoyaltyCards WHERE CustomerID = ?", (customer_id,))
        loyalty_card = cursor.fetchone()
        if loyalty_card:
            print(f"Бонусна картка: {loyalty_card}")
    else:
        print("Клієнта не знайдено.")


# 4.2: Eager Loading
def get_customer_with_loyalty_card_eager(connection):
    cursor = connection.cursor()

    # Завантаження клієнтів разом з їх бонусними картками
    query = """
    SELECT Customers.Name, LoyaltyCards.BonusPoints 
    FROM Customers
    JOIN LoyaltyCards ON Customers.CustomerID = LoyaltyCards.CustomerID
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    print("Клієнти з бонусними картками:")
    for row in rows:
        print(row)


# 4.3: Explicit Loading
def get_customer_with_loyalty_card_explicit(connection, customer_id):
    cursor = connection.cursor()

    # Завантажуємо основного клієнта
    cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
    customer = cursor.fetchone()

    if customer:
        print(f"Клієнт: {customer}")

        # Explicit loading: Завантажуємо LoyaltyCard вручну
        cursor.execute("SELECT * FROM LoyaltyCards WHERE CustomerID = ?", (customer_id,))
        loyalty_card = cursor.fetchone()
        if loyalty_card:
            print(f"Бонусна картка: {loyalty_card}")
    else:
        print("Клієнта не знайдено.")
