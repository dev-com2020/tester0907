Feature: Usunięcie wpisu z książki adresowej
  Wpisy dodane do książki adresowej mogą zostać usunięte.

  Scenario: Usunięcie wpisu z książki adresowej
        Given Mam książkę adresową
        And Mam wpis dotyczący użytkownika "Janek"
        When Po wydaniu polecenia "contacts del Janek"
        Then wpis nie będzie już widoczny w książce adresowej