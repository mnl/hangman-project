# Micke's hangman game

Det här är ett klassiskt hänga gubbe-spel som kan spelas terminalen.
Programmet väljer ett ord av de cirka 3000 i den bifogade filen.
Spelet går sedan ut på att bokstav för bokstav lista ut ordet.

Flera spelare stöds och då turas spelarna om.

## Projektbeskrivning

Detta program ska demonstera det vi gått igenom under kursen. 
Det innehåller och använder bland annat:

- **Klasser** för instanser av spelare
- **Filläsning** för ord
- **Strängformatering** 
- Interaktiv **inmatning** av tecken
- **Olika typer av loopar** för programflöde
- **Import av andra moduler** exempelvis random och shutil
- **Objektorienterat** för att skilja på logik och presentation

## Dokumentation

Spelet börjar med val av antal spelare. Därefter matas namn in på dessa.
I skärmens vänstra hörn syns vems tur det är. Det högra hörnet visar status samt vilka bokstäder som gissats.
I mitten visas luckor för varje bokstav i ordet som ska gissas.
För varje felaktig gissning kommer figuren på skärmen närmare hängning.
Har ordet inte gissats på 11 försök avslutas gissningen och spelarna får frågan om de vill spela med ett nytt ord.

En rätt gissad bokstav ger 10 poäng, ett gissat ord ger 100 poäng.
Matchpoäng visas efter varje avklarat ord och totalpoängen visas när spelet avslutas.

### Beskrivning av programdelar

För att 