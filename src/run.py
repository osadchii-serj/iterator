from library import Library
from book import Book


def client_code(iterator):
    for category in iterator:
        print(category)


if __name__ == "__main__":
    library = Library()

    list_books = [
        Book("Война и мир", "Лев Толстой", "Роман-эпопея"),
        Book("Путешествия Гулливера", "Джонатан Свифт", "Сатира, фэнтези"),
        Book("Улисс", "Джеймс Джойс", "Модернистский роман"),
    ]

    for book in list_books:
        library.add_book(book)

    client_code(library)
    client_code(library.get_author_iterator())
    client_code(library.get_genre_iterator())
