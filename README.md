# Seminarska naloga: zajemanje podatkov iz spletne strani igre Draftout

[Draftout](https://draftoutmc.com/) je igra, v kateri se dva igralca pomerita v opravljanju 25 ciljev, vsakega od katerih lahko opravi največ en izmed njih. Sestoji iz dveh delov: Drafta, v katerem igralca izmenjaje izbirata te cilje, in dejanske igre, v kateri cilje opravljata.

Projekt s spletne strani Draftouta, na kateri je shranjena zgodovina vseh iger, zajema podatke o igrah določenega igralca in jih nato analizira v datoteki `analiza podatkov.ipynb`.

## Navodila za zagon
Za uporabo sta potrebni knjižnici **selenium** in **pandas**.

Uporabnik v datoteki `main.py` nastavi spremenljivko `name` na ime igralca, ki ga želi analizirati, ter jo nato požene. Nato je ustvarjena datoteka `{name}.csv`, v kateri so združeni podatki vseh iger tega igralca. Za analizo teh podatkov uporabnik požene datoteko `analiza podatkov.ipynb`.


## Delovanje in struktura programa

`main.py` je osnovna datoteka, ki jo požene uporabnik.

`cilji.py` vsebuje funkcijo, ki iz spletne strani zajame seznam vseh ciljev in jih shrani v spremenljivko `objectives`.

`match_id.py` je namenjen zajemanju spletne strani s profilom igralca. Funkcija `match_ids` vrne seznam ID-jev vseh iger analiziranega igralca.

`ekstrakcija.py` ima funkcijo `match_stats`, ki zajame spletno stran igre z določenim ID-jem, ter nato z uporabo regularnih izrazov shrani vse cilje, ki so se pojavili v draftu, ki jih je igralec izbral v draftu, ki so se pojavili v igri, ki jih je igralec opravil, in ki jih je opravil njegov nasprotnik.

`general.py` požene funkcijo `match_stats` na vsakem izmed ID-jev, ki jih vrne funkcija `match_ids`. Nato podatke združi v spremenljivko `data` in jih shrani v datoteko `{name}.csv`.


