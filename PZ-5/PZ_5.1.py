# Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить
# функцией с параметрами. Значения n и m программа должна запрашивать.
def find_series_sum(n, m):
    if m < n:
        return 0
    else:
        series_sum = sum(range(n, m + 1))
        return series_sum

n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))

result = find_series_sum(n, m)
print(f"Сумма чисел от {n} до {m} равна {result}")
