# Seminarska naloga: scrapanje spletne strani igre Draftout

[Draftout](https://draftoutmc.com/) je igra, v kateri se dva igralca pomerita v opravljanju 25 ciljev, vsakega izmed katerih lahko opravi največ en izmed njih. Sestoji iz dveh delov: Drafta, v katerem igralca izmenjaje izbirata te cilje, in dejanske igre, v kateri cilje opravljata.

Projekt iz spletne strani Draftouta, na kateri je shranjena zgodovina vseh iger, scrapa podatke o igrah določenega igralca in jih nato analizira v datoteki `analiza podatkov.ipynb`.

# Navodila za zagon
Uporabnik v datoteki `main.py` nastavi spremenljivko `name` na ime igralca, ki ga želi analizirati, ter jo nato požene. Delovanje programa lahko za igralce z veliko igrami traja dolgo časa. Nato je ustvarjena datoteka `{name}.csv`, v kateri so združeni podatki vseh iger tega igralca. Za analizo teh podatkov uporabnik požene datoteko `analiza podatkov.ipynb`.


# Delovanje in struktura programa

`main.py` je osnovna datoteka, ki jo požene uporabnik

`cilji.py` vsebuje funkcijo, ki iz spletne strani scrapa seznam vseh ciljev in jih shrani v spremenljivko `objectives`

`match_id.py` je namenjen scrapanju spletne strani s profilom igralca. Funkcija `match_ids` vrne seznam IDjev vseh iger analiziranega igralca.

`ekstrakcija.py` ima funkcijo `match_stats`, ki scrapa spletno stran igre z določenim IDjem, ter nato z uporabo regularnih izrazov shrani vse cilje, ki so se pojavili v draftu, ki jih je igralec izbral v draftu, ki so se pojavili v igri, ki jih je igralec opravil, ki jih je njegov nasprotnik opravil.

`general.py` požene funkcijo `match_stats` na vsakem izmed IDjev, ki jih vrne funkcija `match_ids`. Nato podatke združi v spremenljivko `data` in jih nato shrani v datoteko `{name}.csv`


