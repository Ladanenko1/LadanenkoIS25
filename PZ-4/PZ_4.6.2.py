def count_segments(A, B):
    count = 0


    while A >= B:
        A -= B
        count += 1

    return count


A_value = int(input("Введите длину первого отрезка: "))
B_value = int(input("Введите длину второго отрезка: "))
result = count_segments(A_value, B_value)
print(f"Количество отрезков B на отрезке A: {result}")
