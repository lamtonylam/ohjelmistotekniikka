# FIFA Elo ranking app

Sovelluksen avulla käyttäjien on mahdollista pitää kirjaa esimerkiksi toimiston tai vaikka ainejärjestön parhaimmista FIFA-pelin pelaajista. Pelaajat saavat ELO-rankingin, joka muuttuu jokaisen tuloksen jälkeen. Mitä isompi piste-erotus pelaajilla on, sitä dramaattisemmin ELO muuttuu ylös tai alas.

Sovelluksesta voi viedä omalle tietokoneellensa PDF-tiedostona exportin sovellukseen tallennetuista tiedoista (pelaajat ja matsit).

## Release

#### [Viikon 5 release](https://github.com/lamtonylam/ohjelmistotekniikka/releases/tag/viikko5)

#### [Viikon 6 release](https://github.com/lamtonylam/ohjelmistotekniikka/releases/tag/viikko6)

#### [Lopullinen release](https://github.com/lamtonylam/ohjelmistotekniikka/releases/tag/final)

# Dokumentaatio

### [Arkkitehtuuri](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/arkkitehtuuri.md)

### [Käyttöohje](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/kayttoohje.md)

### [Vaatimusmäärittely](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/vaatimusmaarittely.md)

### [Tuntikirjanpito](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/tuntikirjanpito.md)

### [Changelog](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/changelog.md)

### [Testausdokumentti](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/testaus.md)

### [Tekoälyn käyttö](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/tekoaly.md)

# Asennus

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

# Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon.

### Testikattavuuden kuva ja badge

Testikattavuudesta voi generoita kuvan ja badgen, joka päivittyy suoraan testausdokumenttiin komennoilla:

Linux:

```bash
sudo apt update
sudo apt install poppler-utils
```

MacOS:

> [!IMPORTANT]  
> huom Brew pitää olla asennettuna
> asenna se [täältä](https://brew.sh/)

```bash
brew install poppler pango cairo weasyprint
```

Ja sitten suorita

```bash
poetry run invoke coverage-image
```

### Pylint

Koodin staattisen analyysin voi suorittaa komennolla:

```bash
poetry run invoke lint
```

### Docstring-kattavuus

Docstringien koodikattavuuden voi generoida komennolla

```bash
poetry run invoke docstring
```

Tulokset tulostuvat suoraan terminaaliin
