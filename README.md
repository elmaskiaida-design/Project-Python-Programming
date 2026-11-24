# Project-Python-Programming: Boeken-, Series- en Filmtracker

## Omschrijving
Dit is een Python-programma waarmee je boeken, series en films bijhoudt.
Je kunt items toevoegen en bekijken via een menu. De gegevens worden
opgeslagen in een JSON-bestand, zodat ze bewaard blijven na het afsluiten.
Het programma berekent ook statistieken, toont een grafiek per maand en geeft
suggesties op basis van je stemming.

## Functies
- Items toevoegen en tonen via een menu (boek, serie, film)
- Opslaan en inlezen met JSON-bestand
- Berekenen van statistieken
- Via `matplotlib` een grafiek per maand
- Exception handling met `try` en `except`
- Suggesties volgens stemming met een dictionary
- Via de Open Library-API boeksuggesties geven

## Projectstructuur
- `main.py`= Hoofdprogramma en het menu
- `Item`= zelf geschreven klasse
- `Boek`, `Serie`, `Film`= Afgeleide klassen van klasse `Item`

## Gebruik en de installatie
1) Deze repository clonen
2) De packages installeren: `pip install matplotlib requests`
3) Het programma starten: `python main.py`
    
## Status
Het project is nog in ontwikkeling, de functies worden stap per stap toegevoegd.

## Auteur
Aida El Maski
