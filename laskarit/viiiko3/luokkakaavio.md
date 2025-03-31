```mermaid
classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

   Ruutu "40" -- "1" Aloitusruutu
   Ruutu "40" -- "22" Katu
   Ruutu "40" --  "1" Vankila
   Ruutu "40" --  "3" Sattuma
   Ruutu "40" --  "3" Yhteismaa
   Ruutu "40" --  "4" Asema
   Ruutu "40" --  "2" Laitos

   Pelaaja "1" -- "*" Katu
   Katu "1" -- "0..4" Talo
   Katu "1" -- "0.." Hotelli

   Pelaaja "1" -- "*" Rahaa

   Toiminto "*" -- "1" Aloitusruutu
      Toiminto "*" -- "1" Katu
         Toiminto "*" -- "1" Vankila
            Toiminto "*" -- "1" Sattuma
               Toiminto "*" -- "1" Asema
                  Toiminto "*" -- "1" Laitos
                     Toiminto "*" -- "1" Katu
```