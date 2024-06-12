n = int(input('Введите кол-во чисел для обработки: '))
arr = [int(input('Введите число: ')) for i in range(n)]
ans = []
max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j] and (arr[i] + arr[j]) % 120 == 0:
            sum = arr[i] + arr[j]
            if sum > max_sum:
                max_sum = sum
                ans = [arr[i], arr[j]]

print(f'Самые большие числа которые делятся на 120, при условии что первое число больше второго: {ans}')
