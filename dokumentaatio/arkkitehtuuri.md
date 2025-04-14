# Arkkitehtuurikuvaus


![](./kuvat/pakkauskaavio.jpg)

Sekvenssikaavio käyttäjän luomisesta

```
mermaid
sequenceDiagram
  actor User_person
  participant UI
  participant EloService
  participant UserRepository
  participant User


  User_person ->> UI: User clicks create User
  UI ->> EloService: create_user("tony123")
  EloService ->> UserRepository: find_user_by_username("tony123")
  UserRepository -->> EloService: User
  EloService ->> User: User(name)
  User -->> EloService: User
  EloService ->> UserRepository: create_user(User)
  UserRepository -->> EloService: User
  UI ->> UI: refresh_player_table()
```