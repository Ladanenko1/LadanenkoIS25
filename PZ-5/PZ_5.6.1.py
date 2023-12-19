def find_series_sum(n, m):
    if m < n:
        return 0  # Возвращаем 0, если m < n
    else:
        series_sum = sum(range(n, m + 1))  # Используем функцию sum для суммирования чисел от n до m
        return series_sum

# Запрос значений n и m у пользователя
n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))

result = find_series_sum(n, m)
print(f"Сумма чисел от {n} до {m} равна {result}")
