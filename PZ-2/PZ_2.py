#Дано трехзначное число.Найти сумму и произведение его цифр.
try:
    num = int(input('Введите трехзначное число: '))
    if num > 99 and num < 1000:
        last = (num % 100) % 10
        middle = (num // 10) % 10
        first = num // 100
        summ = last + middle + first
        equal = last * middle * first
        print(summ, equal)
    else:
        exit()
except:    print("Неправильно введено")
