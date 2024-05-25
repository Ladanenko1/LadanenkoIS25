
import re


with open('price.txt', 'r') as file:
    text = file.read()
    price = re.findall(r'[0-9]+', text)

    print(price)
    count = len(price)

    print("Количество ценников:", count)
