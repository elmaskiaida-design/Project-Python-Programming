from datetime import date

class Item:
    def __init__(self, titel, genre, rating, datum=None):
        self.titel = titel
        self.genre = genre
        self.rating = rating
        self.datum = datum if datum else date.today()
        self.status = "bezig"

    def voortgang(self):
        return 0.0

    def __str__(self):
        return f"{self.titel} ({self.genre}), rating {self.rating}"


class Boek(Item):
    def __init__(self, titel, genre, rating, paginas_totaal, paginas_gelezen=0, datum=None):
        super().__init__(titel, genre, rating, datum)
        self.paginas_totaal = paginas_totaal
        self.paginas_gelezen = paginas_gelezen

    def voortgang(self):
        if self.paginas_totaal == 0:
            return 0.0
        return self.paginas_gelezen / self.paginas_totaal * 100


if __name__ == "__main__":
    boek = Boek("De Hobbit", "Fantasy", 9, 300, 150)
    print(boek)
    print(f"Voortgang: {boek.voortgang():.0f}%")