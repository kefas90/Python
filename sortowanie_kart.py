"""
Sortowanie kart. Funkcja sortujaca kolekcje kart (liste, krotke, itp.).
Funkcja powinna zwracac liste kart posortowanych w kolejnosci od najmniej do najbardziej wartosciowej.
Kolor kart nie jest istotny.

Karty sa reprezentowane przez liczby (int) lub napisy (string):
karty od 2 do 10 to liczby, as to "A", walet to "J", krolowa to "Q", krol to "K"; nie ma jokera.
As ma najmniejsza wartosc, krol najwieksza.

Przyklad posortowanej listy:
['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
"""


letter_cards = {
    "A": 1,
    "J": 11,
    "Q": 12,
    "K": 13
}


def sorting(arg):
    return sorted(arg, key=lambda x: letter_cards[x] if x in letter_cards else x)

cards = ["Q", 2, 7, 10, "J", "A", 2, 4, 4, "A", 7, 3, "K"]
cards2 = (2, "A", "J", 4, 3, "K", 2, 4, 7, "Q", 3, 4, 3, "Q")
print(sorting(cards))
print(sorting(cards2))

