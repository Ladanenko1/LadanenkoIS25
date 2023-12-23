def summa(a, b):
    if a != 2:
        return "false"
    if b != 2:
        return "false"
    else:
        return a + b
numb_one = int(input("Введи 2: "))
numb_two = int(input("Введи еще раз: "))
resuit = summa(numb_one, numb_two)
print(f"Сумма равна {resuit}")
