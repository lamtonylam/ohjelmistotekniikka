# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne noudattelee kolmitasoista kerrosarkkitehtuuria, jossa on eriteltynä, tämä myös noudattelee repositories tiedonkäsittelyn suunnittelumenetelmää.

![](./kuvat/pakkauskaavio.jpg)

Pakkaus ui sisältää käyttöliittymästä, services sovellus/business-logiikasta ja repositories tietojen pysyväistallennuksesta vastaavan koodin. Pakkaus entities sisältää luokkia, jotka kuvastavat sovelluksen käyttämiä tieto-objekteja.


## Käyttöliittymä
Käyttöliittymä sisältää kolme erilaista näkymää:
- Etusivu
- Matsien tallennussivu
- PDF-tiedoston vientisivu

Jokainen näistä näkymistä on toteutettu omana luokkanaan. Näkymät sijaitsevat ´src/ui/views´polussa.

## Päätoiminnallisuuden sekvenssikaavioita


### Sekvenssikaavio uuden käyttäjän luomisesta, olemassaolevaa samannimistä käyttäjää ei ole.

```mermaid
sequenceDiagram
  actor User_person
  participant UI
  participant EloService
  participant UserRepository
  participant User


  User_person ->> UI: User clicks create User
  UI ->> EloService: create_user("tony123")
  EloService ->> UserRepository: find_user_by_username("tony123")
  UserRepository -->> EloService: None
  EloService ->> User: User(name)
  User -->> EloService: User
  EloService ->> UserRepository: create_user(User("tony123))
  UserRepository -->> EloService: User
  UI ->> UI: refresh_player_table()
```


### Sekvenssikaavio PDF-tiedoston exporttaamisesta tietokoneelle

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant PdfExportView
  participant PdfService
  participant EloService
  participant MatchService
  participant FileDialog

  User ->> UI: User clicks "Export to PDF" from main view
  UI ->> PdfExportView: _show_pdf_export_view()
  PdfExportView -->> UI: view
  User ->> PdfExportView: User clicks "Export to pdf" button
  PdfExportView ->> FileDialog: filedialog.asksaveasfilename()
  FileDialog -->> User: Filedialog is showed to user
  User ->> FileDialog: filepath where PDF-document is to be saved
  FileDialog -->> PdfExportView: file_path
  PdfExportView ->> PdfService: generate_pdf(file_path)
  PdfService ->> EloService: get_all_users()
  EloService -->> PdfService: users
  PdfService ->> MatchService: get_all_matches()
  MatchService -->> PdfService: matches
  PdfService ->> PdfService: _draw_title()
  PdfService ->> PdfService: _draw_users(users)
  PdfService ->> PdfService: _draw_matches(matches)
  PdfService ->> PdfService: Save PDF file
  PdfService -->> PdfExportView: PDF saved

```

## Sovelluslogiikka

Sovelluksen loogisen tietomallin muodostavat luokat `User` ja `Match`, jotka kuvaavat käyttäjiä ja heidän välisiä FIFA-otteluita:

```mermaid
classDiagram
    Match "*" --> "1" User : winner
    Match "*" --> "1" User : loser
    class User{
        id
        name
        elo_rating
    }
    class Match{
        id
        winner
        loser
        date
    }
```

Sovelluksen toiminnallisista kokonaisuuksista vastaavat luokat `EloService`, `MatchService` ja `PdfService`. Nämä tarjoavat käyttöliittymälle metodeja eri toimintoihin:

**EloService:**
- `create_user(name)`
- `get_all_users()`
- `find_user_by_id(user_id)`
- `find_user_by_username(username)`
- `update_user_elo(user_id, elo)`

**MatchService:**
- `create_match(winner_username, loser_username)`
- `compute_elo_ratings(winner_id, loser_id)`
- `find_match_by_id(id)`
- `get_all_matches()`

**PdfService:**
- `generate_pdf(filepath)`

Luokat pääsevät käsiksi käyttäjiin ja otteluihin tietojen tallennuksesta vastaavan pakkauksessa _repositories_ sijaitsevien luokkien `UserRepository` ja `MatchRepository` kautta. Luokkien toteutukset injektoidaan sovelluslogiikalle konstruktorikutsun yhteydessä.

## Tietojen pysyväistallennus
Pakkauksen repositories luokat `MatchRepository`ja `UserRepository` huolehtivat ohjelman tietojen tallentamisesta. Kummatkin luokat tallentavat tiedot SQLite-tietokantaan. SQLite on pysyväistallenus, eli sovelluksen tiedot pysyvät niin kauan, kunnes .db tiedosto poistetaan tai alustetaan manuaalisesti tietokanta uusiksi.

Luokat noudattavat Repository -suunnittelumallia. Tämä suunnittelumalli mahdollistaa sen, että tulevaisuudessa halutaan vaihtaa sovelluksen datan tallennustapaa, niin se onnistuu suhteellisen helposti.

### Tiedostot

Sovellus tallentaa tiedot database.db nimiseen tiedostoon, joka sijaitsee projektin juuressa.
