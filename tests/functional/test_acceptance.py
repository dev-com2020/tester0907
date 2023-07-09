from src import contacts


class TestAddingEntries:
    def test_basic(self):
        app = contacts.Application()
        app.run("contacts add Jan Kowalski 123456789")

        assert app._contacts == [
            ("Jan Kowalski", "123456789")
        ]