

# Ohjelmistotekniikka, harjoitustyö
Minulla on ajatuksena tehdä FIFA pelin **ELO** *ranking* työpöytäohjelmisto.
Käyttäjät siis pelaavat oikeassa elämässä FIFA pelimatsin ja sen jälkeen kirjaavat tuloksen ja ELO rankingit muuttuvat.

## Release
#### [Viikon 5 release](https://github.com/lamtonylam/ohjelmistotekniikka/releases/tag/viikko5)  
#### [Viikon 6 release](https://github.com/lamtonylam/ohjelmistotekniikka/releases/tag/viikko6)

# Dokumentaatio
### [Arkkitehtuuri](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/arkkitehtuuri.md)  
### [Käyttöohje](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/kayttoohje.md)  
### [Vaatimusmäärittely](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/vaatimusmaarittely.md)  
### [Tuntikirjanpito](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/tuntikirjanpito.md)
### [Changelog](https://github.com/lamtonylam/ohjelmistotekniikka/blob/main/dokumentaatio/changelog.md)

# Asennus
> [!IMPORTANT]  
> Tarvitset koneellesi Python version 3.9 tai uudemman, jotta voit suorittaa ohjelman.

1. Asenna riippuvuudet komennolla:

```bash
poetry install --no-root
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


### Pylint

Koodin staattisen analyysin voi suorittaa komennolla:

```bash
poetry run invoke lint
```
