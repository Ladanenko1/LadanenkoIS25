import pickle
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

    def __str__(self):
        return f"{self.title} {self.author} {self.pages}"

# Пример использования:
book = Book("1984", "Джордж Оруэлл", 328)
book.read_book()

book.write_book("Скотный двор", "Джордж Оруэлл", 112)
book.read_book()

def save_books(book_list):
    with open('books_data.pkl', 'wb') as f:
        pickle.dump(book_list, f)

def load_books():
    try:
        with open('books_data.pkl', 'rb') as f:
            book_list = pickle.load(f)
        return book_list
    except FileNotFoundError:
        return []

book1 = Book("1984", "Джордж Оруэлл", 328)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", 671)

books = [book1, book2]
save_books(books)

loaded_books = load_books()
for book in loaded_books:
    print(book.__str__())
