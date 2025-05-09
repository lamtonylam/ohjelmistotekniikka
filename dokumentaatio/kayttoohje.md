# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/lamtonylam/ohjelmistotekniikka/releases/) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.


## Ohjelman käynnistäminen

> [!IMPORTANT]  
> Tarvitset koneellesi Python version 3.9 tai uudemman, jotta voit suorittaa ohjelman.

1. Asenna riippuvuudet komennolla:

```bash
poetry install --no-root
```

> [!TIP]
> Jos haluat määritellä itse SQLite-tietokantatiedoston nimen, luo `.env` tiedosto ja luo sinne seuraavat arvot:
> 
> ```
> DATABASE_FILE_NAME="OMA_TIEDOSTO_NIMESI.db"
> TEST_DATABASE_FILE_NAME="OMA_TESTITIEDOSTO_NIMESI.db"
> ```
>
> Vaihtoehtoisesti voit myös jättää arvot määrittelemättä, jolloin sovellus asettaa tiedoston nimeksi oletukset.

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```



## Aloitus
Sovellus käynnistyy alkunäkymään:
![](./kuvat/käyttöohje/kayttoohje1.jpeg)

Matsin tallentamiseksi, paina nappia "Record a match"
PDF-exporttaukseen, paina nappia "Export to PDF"

## Matsin tallentaminen
![](./kuvat/käyttöohje/kayttoohje2.jpeg)

Matsin tallentamiseksi, syötä "Player 1" ja "Player 2" tekstikenttiin pelaajien nimet, ja valitse nappulasta kumpi voitti matsin ja paina "submit". Pelaajien nimet eivät saa olla samoja. Jos pelaajia ei ole luotu vielä sovellukseen, matsin tallentaminen hoitaa sen automaattisesti ja luo ne.

Voit halutessasi myös luoda pelaajan manuaalisesti, jolloin ELO-ranking alkaa 1500:sadasta.  
Kirjoita "insert name of player" tekstikenttään pelaajan nimi ja paina "create"

## PDF-tiedoston vienti

![](./kuvat/käyttöohje/kayttoohje3.jpeg)

PDF-tiedoston vientiin, paina nappia "Export to pdf"

![](./kuvat/käyttöohje/kayttoohje4.jpeg)

Tämän jälkeen valitse haluamasi tiedostopolku ja vietävälle PDF-tiedostolle tiedostonimi ja paina "save" nappulaa.
