def ulam_digits(a=1, b=None, max_count=None):
    ulam_seq = [1, 2]

    if b is None:
        b = float('inf')  # Установим b в бесконечность, если не задано

    while True:
        next_num = ulam_seq[-1] + ulam_seq[-2]

        if next_num >= b:
            break

        ulam_seq.append(next_num)

        if max_count is not None and len(ulam_seq) >= max_count:
            break

    return [num for num in ulam_seq if num >= a]


def main():
    while True:
        try:
            user_input = input(
                "Введите a, b и максимальное количество чисел (разделяя пробелами) или 'стоп' для выхода из программы: ")
            if user_input.lower() == 'стоп':
                print("Завершение программы...")
                break

            # Обработка входных данных
            inputs = list(map(str.strip, user_input.split()))
            if len(inputs) != 3:
                raise ValueError("Необходимо ввести три значения: a, b и максимальное количество чисел.")

            # Преобразуем входные данные
            a = int(inputs[0])
            b = int(inputs[1])
            max_count = int(inputs[2])

            # Проверка условий
            if a >= b:
                raise ValueError("Значение 'a' должно быть меньше 'b'.")
            if max_count <= 0:
                raise ValueError("Максимальное количество должно быть положительным числом.")

            # Вызов функции и вывод результатов
            result = ulam_digits(a, b, max_count)
            print(f"Числа Улама в интервале [{a}, {b}):", result)

        except ValueError as e:
            print(f"Ошибка ввода: {e}")


if __name__ == '__main__':
    main()

