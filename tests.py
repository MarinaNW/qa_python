import pytest

class TestBooksCollector:

    def test_add_new_book_positive_result(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('long_name', [
        ("a" * 41),
        ("a" * 42),
        ("a" * 50),
        ("a" * 100)
    ])
    def test_add_new_book_long_name_negative_result(self, collector, long_name):
        collector.add_new_book(long_name)

        truncated_name = long_name[:40]
        assert long_name not in collector.books_genre and truncated_name not in collector.books_genre


    def test_set_book_genre_positive_result(self, collector):
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.books_genre["Книга1"] == "Фантастика"

    def test_get_book_genre_positive_result(self, collector):
        collector.add_new_book("Книга1")
        collector.set_book_genre("Книга1", "Фантастика")
        assert collector.get_book_genre("Книга1") == "Фантастика"

    def test_get_book_genre_negative_result(self, collector):
        assert collector.get_book_genre("Неизвестная книга") is None

    @pytest.mark.parametrize('genre, expected_books', [
        ('Фантастика', ['Книга1']),
        ('Ужасы', [])
    ])
    def test_get_books_with_specific_genre_positive_result(self,collector, genre, expected_books):
        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        assert collector.get_books_with_specific_genre(genre) == expected_books


    def test_get_books_genre_positive_result(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Ужасы")
        assert collector.get_books_genre() == {"Книга 1": "Фантастика", "Книга 2": "Ужасы"}


    def test_get_books_for_children_positive_result(self, collector):

        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")

        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 2","Мультфильмы" )

        collector.add_new_book("Книга 3")
        collector.set_book_genre("Книга 3", "Детективы")

        collector.add_new_book("Книга 4")
        collector.set_book_genre("Книга 4", "Ужасы")


        expected_books = ["Книга 1", "Книга 2"]

        assert expected_books == collector.get_books_for_children()


    def test_add_book_in_favorites_positive_result(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        assert collector.get_list_of_favorites_books() == ["Книга 1"]

    def test_delete_book_from_favorites_positive_result(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_book_in_favorites("Книга 1")
        collector.delete_book_from_favorites("Книга 1")
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_positive_result(self, collector):
        book_names = ["Книга 1", "Книга 2", "Книга 3"]
        favorite_book_names = ["Книга 1", "Книга 3"]
        for book in book_names:
            collector.add_new_book(book)
        for book in favorite_book_names:
            collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == favorite_book_names



