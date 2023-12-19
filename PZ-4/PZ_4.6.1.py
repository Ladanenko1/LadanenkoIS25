def calculate_expression(A, N):
    result = 0
    power_of_A = 1

    for i in range(N + 1):
        result += ((-1) ** i) * power_of_A
        power_of_A *= A

    return result

A_value = int(input("Введите первое число: "))
N_value = int(input("Введите второе число: "))
result = calculate_expression(A_value, N_value)
print(f"Значение выражения при A={A_value} и N={N_value} равно {result}")
