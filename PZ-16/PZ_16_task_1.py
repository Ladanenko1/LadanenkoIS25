class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read_book(self):
        print(f"Читаем книгу: {self.title} автора {self.author}. Всего страниц: {self.pages}")

    def write_book(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"Книга обновлена: {self.title} автора {self.author}. Всего страниц: {self.pages}")

# Пример использования:
book = Book("1984", "Джордж Оруэлл", 328)
book.read_book()

book.write_book("Скотный двор", "Джордж Оруэлл", 112)
book.read_book()
