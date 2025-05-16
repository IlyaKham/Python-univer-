def main():
    while True:
        firma = {}
        for i in range(4):
            while True:
                try:
                    name = input(f"Введите название магазина {i + 1} (или 'стоп' для выхода): ")
                    if name == 'стоп':
                        print("Выход из программы.")
                        return
                    revenue_input = input(f"Введите выручку за 2 месяца для магазина '{name}' через пробел: ")
                    revenues = list(map(int, revenue_input.split()))
                    if len(revenues) != 2:
                        raise ValueError("Необходимо ввести выручку за два месяца.")
                    firma[name] = revenues
                    break
                except ValueError as e:
                    print(f"Ошибка ввода: {e}. Пожалуйста, попробуйте снова.")

        # Вычисляем среднюю выручку и выводим результаты
        for shop, revenues in firma.items():
            average_revenue = sum(revenues) / 2
            print(f"Средняя выручка за 2 первых месяца магазина '{shop}': {average_revenue} р.")

        # Находим магазин с максимальной выручкой
        total_revenue = {shop: sum(revenues) for shop, revenues in firma.items()}
        max_value = max(total_revenue.values())
        max_key = max(total_revenue, key=total_revenue.get)
        print(f"Максимальная выручка за период составила: {max_value} р., в магазине '{max_key}'")

        # Спросим пользователя, хочет ли он ввести данные еще раз
        repeat = input("Хотите ввести данные еще раз? (да/нет): ").strip().lower()
        if repeat != 'да':
            print("Выход из программы.")
            break


main()