# отобразить исходный словарь и словарь в котором удалены  2 и 3 элементы, используя for и range
dict = {x: x**2 for x in range(7)}

print("Исходный словарь:", dict)
del dict[1]
del dict[2]

print("Получившийся словарь:", dict)