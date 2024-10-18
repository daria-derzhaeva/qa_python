from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize("first_book, second_book", [('Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить')])
    def test_add_new_book_add_two_books(self, first_book, second_book):
        collector = BooksCollector()

        collector.add_new_book(first_book)
        collector.add_new_book(second_book)

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("long_title", ['Удивительные приключения барона Мюнхгаузена на земле, в воде и в воздухе'])
    def test_add_new_book_check_max_len(self, long_title):
        collector = BooksCollector()

        collector.add_new_book(long_title)

        assert long_title not in collector.get_books_genre()
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize("book_name, genre", [("1984", "Фантастика"), ("Дракула", "Ужасы"), ("Властелин колец", "Фантастика")])
    def test_set_book_genre_is_set_for_existing_book(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("book_name", ['Великий гном', 'Невидимый город'])
    def test_get_book_genre_for_non_existing_book(self, book_name):
        collector = BooksCollector()

        assert collector.get_book_genre(book_name) is None

    @pytest.mark.parametrize("books_data, genre, expected_books", [(["1984", "Фантастика"], "Фантастика", ["1984"]), (["Дракула", "Ужасы"], "Ужасы", ["Дракула"]), ([], "Неизвестный жанр", []),])
    def test_get_books_with_specific_existing(self, books_data, genre, expected_books):
        collector = BooksCollector()

        for book_name, book_genre in books_data:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, book_genre)

        books = collector.get_books_with_specific_genre(genre)

        assert books == expected_books

    def test_get_books_genre_empty_before_adding_books(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}

    def test_get_books_for_children_with_appropriate_genres(self):
        collector = BooksCollector()

        collector.add_new_book("Волшебник страны Оз")
        collector.set_book_genre("Волшебник страны Оз", "Фантастика")

        collector.add_new_book("Сказки братьев Гримм")
        collector.set_book_genre("Сказки братьев Гримм", "Мультфильмы")

        collector.add_new_book("Сияние")
        collector.set_book_genre("Сияние", "Ужасы")

        books = collector.get_books_for_children()

        assert books == ["Волшебник страны Оз", "Сказки братьев Гримм"]

    @pytest.mark.parametrize("book_name", ["1984", "Властелин колец", "Дракула"])
    def test_add_book_in_favorites_when_book_in_genre(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        assert book_name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name", ["1984", "Властелин колец"])
    def test_delete_book_from_favorites_book_existed(self, book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        collector.delete_book_from_favorites(book_name)

        assert book_name not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_no_books(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []