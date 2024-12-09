from database import create_connection, create_tables, insert_initial_data
from queries import get_orders_lazy, get_orders_eager, get_orders_explicit, get_total_bonus_points, get_high_value_orders, get_sorted_orders

# Основна функція для запуску програми
def main():
    # Підключаємося до бази даних
    connection = create_connection()

    # Створюємо таблиці, якщо вони ще не існують
    create_tables(connection)

    # Заповнюємо базу тестовими даними
    insert_initial_data(connection)

    # Виконання запитів

    print("1. Lazy Loading:")
    get_orders_lazy(connection)

    print("\n2. Eager Loading:")
    get_orders_eager(connection)

    print("\n3. Explicit Loading:")
    get_orders_explicit(connection)

    print("\n4. Загальна кількість бонусних балів:")
    get_total_bonus_points(connection)

    print("\n5. Фільтрація замовлень з сумою більше 30:")
    get_high_value_orders(connection, 30)

    print("\n6. Сортування замовлень за сумою:")
    get_sorted_orders(connection)

    connection.close()

if __name__ == "__main__":
    main()
