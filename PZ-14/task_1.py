
import re


with open('price.txt', 'r') as file:
    text = file.read()
    prices = re.findall(r'[0-9]+', text)

    print(prices)
    count = len(prices)

    print("Количество ценников:", count)
