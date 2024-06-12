#1. Средствами языка python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt)следующего вида, предварительно выполнив требуемую
#обработку элементов:

#Исходные данные:
#Количество элементов:
#Положительные числа:
#Количество положительных чисел:
#Отрицательные числа
#Количество отрицательных чисел
with open("исходные_данные.txt", "w") as f:

    f.write("10 20 -5 5 -10 25 30")

with open("обработанные_данные.txt", "w", encoding='utf-8') as f:
    positive_count = 0
    negative_count = 0


    numbers = [int(num) for num in open("исходные_данные.txt").read().split()]


    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1


    f.write(f"Количество элементов: {len(numbers)}\n")
    f.write(f"Положительные числа: {positive_count}\n")
    f.write('Положительные числа')
    f.write(" ".join(str(num) for num in numbers if num > 0) + "\n")
    f.write(f"Отрицательные числа: {negative_count}\n")
    f.write('Отрицательные  числа')
    f.write(" ".join(str(num) for num in numbers if num < 0) + "\n")
