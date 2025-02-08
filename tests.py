import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_positive_result(self):
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('long_name', [
        ("a" * 41),  # Длинная строка длиной 42 символа
        ("b" * 42),  # Ещё одна длинная строка для примера
    ])
    def test_add_new_book_long_name_negative_result(self, long_name):
        collector = BooksCollector()
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre


    def test_set_book_genre_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book("Звезда")
        collector.set_book_genre("Звезда", "Фантастика")
        assert collector.books_genre["Звезда"] == "Фантастика"

    def test_get_book_genre_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.get_book_genre("Книга1") == "Фантастика"

    def test_get_book_genre_negative_result(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Неизвестная книга") is None

    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Звезда']),
        ('Ужасы', [])
    ])
    def test_get_books_with_specific_genre_positive_result(self, genre, expected_books):
        collector = BooksCollector()
        collector.add_new_book('Звезда')
        collector.set_book_genre('Звезда', 'Фантастика')
        assert collector.get_books_with_specific_genre(genre) == expected_books


    def test_get_books_genre_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Ужасы")
        assert collector.get_books_genre() == {"Книга 1": "Фантастика", "Книга 2": "Ужасы"}


    def test_get_books_for_children_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        assert collector.get_books_for_children() == ["Книга 1"]

    def test_add_book_in_favorites_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        assert collector.get_list_of_favorites_books() == ["Книга 1"]

    def test_delete_book_from_favorites_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        collector.delete_book_from_favorites("Книга 1")
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_positive_result(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        assert collector.get_list_of_favorites_books() == ["Книга 1"]

