# Из исходного текстового файла (price.txt) выбрать все цены. Посчитать количество полученных элементов.
import re
with open('price.txt', 'r', encoding='utf-8') as file:
    text = file.read()
findall = re.findall(r'\d+.\w+.', text)
with open('findalldigits.txt', 'w') as file:
    file.write(', '.join(findall))
print('Колличество элементов:',len(findall))

