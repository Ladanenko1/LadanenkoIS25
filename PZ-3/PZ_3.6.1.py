#Даны три целых числа, проверить истинность высказывания"Ровно два из чисел являются положительными"
def check_positive_numbers(a, b, c):
    positive_count = 0
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2

A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B: "))
C = int(input("Введите целое число C: "))

result = check_positive_numbers(A, B, C)
print(f"Ровно два из чисел A, B, C являются положительными: {result}") #{} вставляет в код значение переменных(a,b,c)
