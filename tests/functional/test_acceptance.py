from pytest_bdd import scenario, given, parsers, when, then

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


@scenario(r"D:\projekty\tester0907\tests\acceptance\delete_contact.feature", "Usunięcie wpisu z książki adresowej")
def test_deleting_contacts():
    pass

@then("wpis nie będzie już widoczny w książce adresowej")
def emptylist(contactbook):
    assert contactbook._contacts == []

@given("Mam książkę adresową", target_fixture="contactbook")
def contactbook():
    return contacts.Application()

@scenario(r"D:\projekty\tester0907\tests\acceptance\list_contacts.feature",
          "Wyświetlenie listy dodanych wpisów do książki adresowej")
def test_listing_added_contacts(capsys):
    pass

@given(parsers.parse("Mam pierwszy wpis <pierwszy>"))
def have_a_first_contact(contactbook, pierwszy):
    contactbook.add(pierwszy, "123456789")
    return pierwszy

@given(parsers.parse("Mam drugi wpis <second>"))
def have_a_second_contact(contactbook, second):
    contactbook.add(second, "123456789")
    return second

@then(parsers.parse("Dane wyjściowe zawierają listę wpisów <listed_contacts>"))
def outputcontains(listed_contacts, capsys):
    expected_list = "".join([f"{contact} 123456789\n" for contact in listed_contacts.split(",")])
    out, _ = capsys.readouterr()
    assert out == expected_list

@given(parsers.parse("Mam wpis dotyczący użytkownika \"{contactname}\""))
def have_a_contact(contactbook, contactname):
    contactbook.add(contactname, "123456789")

@when(parsers.parse("Po wydaniu polecenia \"{command}\""))
def runcommand(contactbook, command):
    contactbook.run(command)



