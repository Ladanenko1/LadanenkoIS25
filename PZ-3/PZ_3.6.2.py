# Даны три целых числа, одно из которых отлично от двух других, равных между собой.
# Определить порядковый номер числа, отличного от остальных
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
def find_odd_one_out(a, b, c):
    if a == b:
        return 3
    elif a == c:
        return 2
    else:
        return 1
result = find_odd_one_out(a , b, c)
print(f"Число, отличное от остальных, имеет порядковый номер: {result}")
