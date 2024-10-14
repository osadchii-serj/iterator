## Библиотека книг с несколькими итераторами
### Цель: Создать приложение для управления библиотекой, позволяющее пользователям просматривать книги различными способами (по автору, по жанру и т.д.) с помощью разных итераторов. Структура проекта:

    Классы:
        Book: представляет книгу.
        Library: коллекция книг.
        AuthorIterator: итератор для обхода книг по автору.
        GenreIterator: итератор для обхода книг по жанру.
        LibraryIterator: общий итератор для обхода всех книг.
    Методы:
        Library.add_book(book): добавляет книгу в библиотеку.
        Library.get_author_iterator(): возвращает итератор для обхода книг по автору.
        Library.get_genre_iterator(): возвращает итератор для обхода книг по жанру.
        Library.__iter__(): возвращает общий итератор.

### Взаимодействие частей:

    Пользователь добавляет книги в библиотеку через метод add_book.
    Для получения списка авторов или жанров используются соответствующие итераторы (get_author_iterator, get_genre_iterator).
    Общий итератор позволяет перебрать все книги.
