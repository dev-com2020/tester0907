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