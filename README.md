# Mickes Hangman game

Det här är ett klassiskt hänga gubbe-spel som kan spelas terminalen.
Programmet väljer ett ord av de cirka 3000 i den bifogade filen.
Spelet går sedan ut på att bokstav för bokstav lista ut ordet.

Flera spelare stöds och då turas spelarna om.

## Projektbeskrivning

Detta program ska demonstera det vi gått igenom under kursen. 
Det innehåller och använder bland annat:

- **Klasser** för instanser av spelare
- **Filläsning** för ordlista
- **Strängformatering** 
- Interaktiv **inmatning** av tecken
- **Olika typer av loopar** för programflöde
- **Import av andra moduler** som `random` och `shutil`
- **Objektorienterat** för att skilja på logik och presentation
- **Förberett** för att bygga vidare
- På **Github** :octocat: 

## Dokumentation

Spelet börjar med val av antal spelare. Därefter matas namn in på dessa.
I skärmens vänstra hörn syns vems tur det är. Det högra hörnet visar status samt vilka bokstäder som gissats.
I mitten visas luckor för varje bokstav i ordet som ska gissas.
För varje felaktig gissning kommer figuren på skärmen närmare hängning.
Har ordet inte gissats på 11 försök avslutas gissningen och spelarna får frågan om de vill spela med ett nytt ord.

En rätt gissad bokstav ger 10 poäng, ett gissat ord ger 100 poäng.
Matchpoäng visas efter varje avklarat ord och totalpoängen visas när spelet avslutas. :hurtrealbad:

### Beskrivning av programdelar

Klassen `Player` hanterar spelarnas namn och poäng, varje instans är en spelar och det finns ingen gräns för hur många som kan spela.

`TerminalTyper` hanterar all utskrift på skärmen och tar även input. Detta för att lätt kunna byta ut hela denna klass om ett annat interface utvecklas.
`TerminalTyper` är inte så avancerad utan bygger på att terminalen rapporterar sin storlek i rader och kolumner. `Klassen har `update`- och `clear`-metoder som ritar upp de rader som behöver vara på skärmen. `shutil` behövs för att hantera detta.
`textblock` och `hangman` fungerar på samma sätt och måste hålla reda på antalet tecken som skrivs för att hålla innehållet centrerat.

I funktionen `newGame()` finns den mesta logiken för spelet och varje spel om ett ord stannar i while-loopen där inne.
Den gissade bokstaven (`guess`) jämförs mot de redan gissade bokstäverna. Därefter kontrolleras den mot svaret. Efter det kontrolleras den mot alfabetet om det är en bokstav över huvud taget.

Programmet börjar med initiering av spelare och ordlista. Här skapas spelarna och filen öppnas.
