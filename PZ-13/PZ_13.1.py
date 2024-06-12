# 1 в матрице найти суммы элементов  каждой строки и поместить их в новый массив
# выполнить замену элемнтов третьего столбца исходной матрицы на полученные суммы
# в матрице накйти сумму элементов второй половины матрицы
from random import randint

matrix = [[randint(1,10) for i in range(3)]for i in range(3)]
columnsSum = []
n = 0
print(f'Матрица - ', matrix)

for i in range(len(matrix)):
    columnsSum.append(sum(matrix[i]))

for i in matrix:
    i[2] = columnsSum[n]
    n += 1

print(f'Сумма чисел в строках матрицы - ', columnsSum)
print(f'Измененная матрица - ', matrix)
print("Минимальный элемент в предпоследней строке:", min(matrix[-2]))


