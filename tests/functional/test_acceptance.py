from src import contacts


class TestAddingEntries:
    def test_basic(self):
        app = contacts.Application()
        app.run("contacts add Jan Kowalski 123456789")

        assert app._contacts == [
            ("Jan Kowalski", "123456789")
        ]

    def test_surnames_with_spaces(self):
        app = contacts.Application()
        app.run("contacts add Ludwik Mariusz Kowalski 123456789")
        app.run("contacts add Jan Kowalski-Kowalski 123456789")


        assert app._contacts == [
            ("Ludwik Mariusz Kowalski", "123456789"),
            ("Jan Kowalski-Kowalski", "123456789")
        ]

    def test_invalid_strings(self):
        app = contacts.Application()
        app.run("contacts add Jan Kowalski fhiujdshfisdhfihu")
        assert app._contacts == []

    def test_international_numbers(self):
        app = contacts.Application()
        app.run("contacts add Yennefer z Wanderbergu +48123456789")

        assert app._contacts == [
            ("Yennefer z Wanderbergu", "+48123456789")
        ]

    def test_reload(self):
        app = contacts.Application()
        app.run("contacts add Yennefer z Wanderbergu +48123456789")
        assert app._contacts == [
            ("Yennefer z Wanderbergu", "+48123456789")
            ]
        app._clear()
        app.load()
        assert app._contacts == [
            ("Yennefer z Wanderbergu", "+48123456789")
            ]