\# Finansų Sekimo Sistema (Finance Tracking System)



\## Įvadas



Šis kursinis darbas yra finansų sekimo programa, sukurta naudojant Python programavimo kalbą ir objektinio programavimo (OOP) principus.

Programos tikslas - padėti studentams/vartotojamss valdyti savo finansus, registruojant pajamas ir išlaidas, stebint balansą, nustatant limitus bei išsaugant duomenis į failą.



Projektas sukurtas siekiant įgyvendinti kursinio darbo reikalavimus ir pademonstruoti OOP principų, dizaino šablonų, failų valdymo bei testavimo panaudojimą praktikoje.



\---



\## Programos paleidimas



1\. Atidarykite projektą terminale

2\. Paleiskite programą:



```bash

python app.py

```



\---



\## Funkcionalumas



Programa leidžia:



\* Kurti kelis vartotojus

\* Pridėti pajamas ir išlaidas

\* Peržiūrėti balansą ir transakcijų istoriją

\* Šalinti transakcijas

\* Nustatyti dienos, savaitės ir mėnesio limitus

\* Išsaugoti duomenis į JSON failą

\* Įkelti duomenis iš failo

\* Atlikti bendrus (group) įnašus keliems vartotojams



\---



\## Projekto struktūra



\* `models/` – duomenų klasės (User, Wallet, Transaction)

\* `services/` – logika (valdymas, failai, factory)

\* `tests/` – testai

\* `data/` – saugomi JSON duomenys

\* `app.py` – pagrindinis programos failas



\---



\## OOP principai



\### 1. Inkapsuliacija



Duomenys ir funkcijos sujungiami klasėse:



\* `User` saugo vartotojo informaciją

\* `Wallet` saugo balansą ir transakcijas



Tai leidžia kontroliuoti prieigą prie duomenų.



\---



\### 2. Abstrakcija



`Transaction` klasė apibrėžia bendrą struktūrą:



\* suma

\* kategorija

\* aprašymas

\* data



Metodas `apply()` aprašomas abstrakčiai ir realizuojamas paveldėtose klasėse.



\---



\### 3. Paveldėjimas



Naudojamos klasės:



\* `IncomeTransaction`

\* `ExpenseTransaction`



Jos paveldi iš `Transaction` ir perrašo logiką.



\---



\### 4. Polimorfizmas



Skirtingi transakcijų tipai naudoja tą patį metodą `apply()`:



\* pajamos padidina balansą

\* išlaidos sumažina balansą



\---



\## Kompozicija ir agregacija



\* `User` turi `Wallet` (kompozicija)

\* `Wallet` turi `Transaction` sąrašą (kompozicija)

\* `FinanceManager` valdo daug vartotojų (agregacija)



\---



\## Dizaino šablonas



Naudotas \*\*Factory Pattern\*\* (`TransactionFactory`).



Jis leidžia kurti skirtingus transakcijų tipus per vieną metodą:



```python

TransactionFactory.create\_transaction(...)

```



\### Kodėl pasirinktas



\* centralizuoja objektų kūrimą

\* lengva pridėti naujus tipus

\* mažina kodo pasikartojimą



\---



\## Failų skaitymas ir rašymas



Duomenys saugomi JSON formatu:



\* `save\_to\_file()` – išsaugo duomenis

\* `load\_from\_file()` – įkelia duomenis



Failas:



```

data/finance\_data.json

```



\---



\## Limitų sistema



Sistema leidžia nustatyti:



\* dienos limitą

\* savaitės limitą

\* mėnesio limitą



Viršijus limitą, transakcija nėra pridedama.



\---



\## Group deposit funkcija



Programa leidžia vienu metu pridėti pajamas keliems vartotojams.



Tai realizuota metode:



```

group\_deposit()

```



\---



\## Testavimas



Naudotas `unittest` modulis.



Testuojama:



\* transakcijų pridėjimas

\* šalinimas

\* limitų veikimas



Paleidimas:



```bash

python -m unittest discover -s tests

```



\---



\## Rezultatai



\* Sukurta pilnai veikianti finansų sekimo sistema

\* Įgyvendinti visi pagrindiniai reikalavimai

\* Pritaikyti OOP principai ir dizaino šablonas

\* Programa gali būti plečiama ateityje



\---



\## Išvados



Šis projektas padėjo geriau suprasti:



\* objektinį programavimą

\* sistemų struktūrizavimą

\* duomenų saugojimą

\* testavimą



Ateityje sistemą galima išplėsti:



\* pridėti vartotojo sąsają

\* generuoti ataskaitas

\* pridėti grafiką (GUI)



\---



\## Naudoti šaltiniai



\* Python dokumentacija

\* unittest dokumentacija

\* JSON dokumentacija

\* GitHub



