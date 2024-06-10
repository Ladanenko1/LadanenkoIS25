# Открываем файл для записи обработанных данных
with open("обработанные_данные.txt", "w", encoding='utf-8') as f:
    # Инициализируем счетчики
    positive_count = 0
    negative_count = 0

    # Читаем числа из исходного файла
    numbers = [int(num) for num in open("исходные_данные.txt").read().split()]

    # Подсчитываем положительные и отрицательные числа
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    # Записываем результаты в обработанный файл
    f.write(f"Количество элементов: {len(numbers)}\n")
    f.write(f"Положительные числа: {positive_count}\n")
    # Выводим положительные числа
    f.write('Положительные числа')
    f.write(" ".join(str(num) for num in numbers if num > 0) + "\n")
    f.write(f"Отрицательные числа: {negative_count}\n")
    # Выводим отрицательные числа
    f.write('Отрицательные  числа')
    f.write(" ".join(str(num) for num in numbers if num < 0) + "\n")
