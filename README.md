

# Ohjelmistotekniikka, harjoitustyö
Minulla on ajatuksena tehdä FIFA pelin **ELO** *ranking* työpöytäohjelmisto.
Käyttäjät siis pelaavat oikeassa elämässä FIFA pelimatsin ja sen jälkeen kirjaavat tuloksen ja ELO rankingit muuttuvat.


# Dokumentaatio
### [Vaatimusmäärittely](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/vaatimusmaarittely.md)  
### [Tuntikirjanpito](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/tuntikirjanpito.md)
### [Tuntikirjanpito](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/changelog.md)

# Asennus
> [!IMPORTANT]  
> Tarvitset koneellesi Python version 3.9 tai uudemman, jotta voit suorittaa ohjelman.

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

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