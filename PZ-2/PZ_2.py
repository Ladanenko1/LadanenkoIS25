#Дано трехзначное число.Найти сумму и произведение его цифр.
try: # используется для того чтобы пользователь не смог написать текст, иначе ему выдаст  except:
    num = int(input('Введите трехзначное число: '))
    if num > 99 and num < 1000:
        last = (num % 100) % 10 #% остаток от деления 19-5=4
        middle = (num // 10) % 10
        first = num // 100 # целочисленное деление
        summ = last + middle + first
        equal = last * middle * first
        print(summ, equal)
    else:
        exit()
except:
    print("Неправильно введено")
