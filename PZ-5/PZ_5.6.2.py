# Описать функцию Роwer(А, В) вещественного типа, находящую величину АВ по
# формуле АВ = ехр(В*ln(А)) (параметры А и В — вешественные). В случае нулевого
# или отрицательного параметра А функция возвращает 0. С помощью этой функции
# найти степени А^Р, В^Р, С^Р, если даны числа Р, А, В, С
import math

def Power(A, B):
    if A <= 0:
        return 0
    else:
        result = math.exp(B * math.log(A))
        return result

P = int(input("Введите число P: "))
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))
C = int(input("Введите число C: "))


result_A = Power(A, P)
result_B = Power(B, P)
result_C = Power(C, P)

print(f"A^P = {result_A}, B^P = {result_B}, C^P = {result_C}")
