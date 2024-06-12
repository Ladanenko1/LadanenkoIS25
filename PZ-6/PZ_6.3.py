# Дан целочисленный сиисок размера N, содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.
def find_identical_elements_indices(arr):
    indices = {}
    for i in range(len(arr)):
        if arr[i] in indices:
            indices[arr[i]].append(i)
        else:
            indices[arr[i]] = [i]

    for k in sorted(indices.keys()):
        if len(indices[k]) > 1:
            print(f"Повторяющийся элемент {k} имеет индексы: {', '.join(map(str, indices[k]))}")

N = int(input("Введите размер списка N: "))
A = []
for i in range(N):
    element = int(input(f"Введите элемент {i+1}: "))
    A.append(element)

find_identical_elements_indices(A)
