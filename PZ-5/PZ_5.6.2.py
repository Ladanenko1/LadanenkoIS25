import math

def Power(A, B):
    if A <= 0:
        return 0  # Возвращаем 0, если A нулевой или отрицательный
    else:
        result = math.exp(B * math.log(A))  # Вычисляем A^B по формуле A^B = exp(B * ln(A))
        return result

# Дано: значения P, A, B, C
P = int(input("Введите число P: "))
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))


# Нахождение степеней A^P, B^P, C^P с использованием функции Power
result_A = Power(A, P)
result_B = Power(B, P)
result_C = Power(C, P)

print(f"A^P = {result_A}, B^P = {result_B}, C^P = {result_C}")
