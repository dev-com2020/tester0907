Feature: Funkcjonalność - wyświetlanie listy wpisów do książki adresowej
  Wpisy dodane do książki adresowej mogą być wyświetlone w postaci listy.

  Scenario: Wyświetlenie listy dodanych wpisów do książki adresowej
    Given Mam książkę adresową
    And Mam pierwszy wpis <pierwszy>
    And Mam drugi wpis <second>
    When Po wydaniu polecenia "contacts ls"
    Then Dane wyjściowe zawierają listę wpisów <listed_contacts>

    Examples:
    | pierwszy   | second | listed_contacts |
    | Mariusz    | Ludwik | Mariusz,Ludwik  |
    | Janek      | Jerzy  | Janek,Jerzy     |
