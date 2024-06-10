# Открываем файл для чтения
with open("text18-16.txt", "r", encoding='utf-16') as f:
    # Читаем текст из файла и удаляем знаки пунктуации
    text = f.read().replace(".", "!").replace(",", "!").replace(":", "!")

 # Выводим исходный текст
print("Исходный текст:")
print(text)

# Подсчитываем буквы в верхнем регистре
uppercase_count = sum(1 for char in text if char.isupper())

# Выводим количество букв в верхнем регистре
print(f"Количество букв в верхнем регистре: {uppercase_count}")

# Пишем текст в стихотворной форме
with open("стихотворение.txt", "w", encoding='utf-8') as f:
    f.write(text)

