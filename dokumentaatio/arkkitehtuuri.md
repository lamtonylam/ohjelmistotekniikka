# Arkkitehtuurikuvaus


![](./kuvat/pakkauskaavio.jpg)

Sekvenssikaavio käyttäjän luomisesta

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
  EloService ->> UserRepository: create_user(User("tony123)
  UserRepository -->> EloService: User
  UI ->> UI: refresh_player_table()
```


## Tietojen pysyväistallennus
Pakkauksen repositories luokat `MatchRepository`ja `UserRepository` huolehtivat ohjelman tietojen tallentamisesta. Kummatkin luokat tallentavat tiedot SQLite-tietokantaan. SQLite on pysyväistallenus, eli sovelluksen tiedot pysyvät niin kauan, kunnes .db tiedosto poistetaan tai alustetaan manuaalisesti tietokanta uusiksi.

Luokat noudattavat Repository -suunnittelumallia. Tämä suunnittelumalli mahdollistaa sen, että tulevaisuudessa halutaan vaihtaa sovelluksen datan tallennustapaa, niin se onnistuu suhteellisen helposti.

### Tiedostot

Sovellus tallentaa tiedot database.db nimiseen tiedostoon, joka sijaitsee projektin juuressa.
