# Дана строка-предложение на русском языке. Преобразовать строку так, чтобы каждое слово начиналось с
# заглавной буквы. Словом считать набор символов, не
# содержащий пробелов и ограниченный пробелами или началом/конном строки.
# Слова, не начинающиеся с буквы, не изменять.
input_string = input("Введите предложение: ")
formatted_string = input_string.title()
print(formatted_string)
