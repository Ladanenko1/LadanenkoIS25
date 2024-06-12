# Дано вещественное число A и целое число N(>0).
# Используя один цикл, найти значение выражения 1 - A + A^2 - A^3 + ... +(-1)^N A^N.
# Условный оператор не использовать.
def calculate(A, N):
    result = 0
    power_of_A = 1

    for i in range(N + 1): # здесь i принимает значения от 0 до N, а цикл валируется в последовательность N + 1
        result += ((-1) ** i) * power_of_A #умножает i каждый раз на -1,для того чтобы чередовать знаки
        power_of_A *= A # умножает power_of_A на A

    return result

A_value = int(input("Введите первое число: "))
N_value = int(input("Введите второе число: "))
result = calculate(A_value, N_value)
print(f"Значение выражения при A={A_value} и N={N_value} равно {result}")
