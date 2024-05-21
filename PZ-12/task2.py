#Составить генератор (yield), который переведёт символы строки из нижнего регистра в верхний.
line = "ПриВет, Я сЪехАл нА квАрТиРУ Год НазАД!"

def upper_generator(str):
    for char in str:
        if char.islower():
            yield char.title()
        else:
            yield char

result = ''.join(upper_generator(line))
print(result)
