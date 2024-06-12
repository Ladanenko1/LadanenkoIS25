#2. Из предложенного текстового файла (text18-16.txt) вывести на экран его содержимое,
#количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст
#в стихотворной форме предварительно заменив все знаки пунктуации на знак «!».
with open("text18-16.txt", "r", encoding='utf-16') as f:

    text = f.read().replace(".", "!").replace(",", "!").replace(":", "!")


print("Исходный текст:")
print(text)


uppercase_count = sum(1 for char in text if char.isupper())


print(f"Количество букв в верхнем регистре: {uppercase_count}")


with open("стихотворение.txt", "w", encoding='utf-8') as f:
    f.write(text)

