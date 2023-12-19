def find_identical_elements_indices(arr):
    indices = {}  # Используем словарь для хранения индексов одинаковых элементов
    for i in range(len(arr)):
        if arr[i] in indices:
            indices[arr[i]].append(i)  # Добавляем индекс в список для данного элемента
        else:
            indices[arr[i]] = [i]  # Создаем список индексов для элемента, если он встречается впервые

    for k in sorted(indices.keys()):
        if len(indices[k]) > 1:  # Выводим индексы только для повторяющихся элементов
            print(f"Повторяющийся элемент {k} имеет индексы: {', '.join(map(str, indices[k]))}")

# Запрашиваем целочисленный список размера N у пользователя и вызываем функцию для нахождения индексов
N = int(input("Введите размер списка N: "))
A = []
for i in range(N):
    element = int(input(f"Введите элемент {i+1}: "))
    A.append(element)

find_identical_elements_indices(A)
