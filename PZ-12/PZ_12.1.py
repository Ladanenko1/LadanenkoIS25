#В последовательности на n целых чисел умножить все элементы на первый элемент
import random
a_len = random.randint(3, 5)
a = [random.randint(2, 10) for _ in range(a_len)]

def umn_na_first(seq):
    first_element = seq[0]
    umn_na_first = [element * first_element for element in seq]
    return umn_na_first

print("Исходная последовательность:", a)
print("Результат умножения на первый элемент:", umn_na_first(a))
