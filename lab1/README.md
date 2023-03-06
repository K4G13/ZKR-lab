# Szyfr Playfair

---
## :book: Wikipedia: *https://pl.wikipedia.org/wiki/Szyfr_Playfair*

---
## Zasady budowania szyfru
Polega on na zastąpieniu par liter tekstu jawnego inną parą liter. Użyjmy jako słowa-klucza słowa **SZYFR**. Pierwszą czynnością będzie zapisanie liter alfabetu w kwadracie 5 x 5, zaczynając od słowa kluczowego i łącząc litery **I** oraz **J**.

| **S** | **Z** | **Y** | **F** | **R** |
| --- | --- | --- | --- | --- |
| A | B | C   | D | E |
| G | H | I/J | K | L |
| M | N | O   | P | Q |
| T | U | V   | W | X |

Jeżeli chcielibyśmy użyć słowa **KAJAK** jako słowo-klucz musimy pominąć powtarzające się litery (czyli: **KAJ**).

Następnie musimy podzielić tekst do zaszyfrowania na pary liter. Każda z par powinna się skłądać z dwóch różnych od siebie liter. W razie potrzeby możemy wstawić **X** w wybranej przez nas parze.

Przykład:
tekst jawny: **politechnika poznanska**
tekst jawny podzielony na pary: **po-li-te-ch-ni-ka-po-zn-an-sk-ax**

Teraz możemy przystąpić do szyfrowania. Robimy to na podstawie trzech reguł:
1. **Jeżeli obie litery są w tym samym wierszu**
    bierzym następniki tych liter znajdujące się o jedną kratke w prawo od nich (naszą talbicę traktujemy jakby prawa krawędź łączyła się z lewą).
    np: **on** => **PO** , **pq** => **QM**
    <br>
2. **Jeżeli obie litery są w tej samej kolumnie** 
    bierzym następniki tych liter znajdujące się o jedną kratke w dół od nich (naszą talbicę traktujemy jakby dolna krawędź łączyła się z górną).
    np: **le** => **QL** , **xr** => **RE**
    <br>
3. **Inne przypadki**
    wyznaczamy prostokąt o wierzchołkach w podanych literach a następnie dobieramy do nich litery należące do tych samych wierszy oraz tworzącymi z nimi wierzchołki owego prostkąta.
    np: **HW** tworzy prostokąt:
    |   |   |   |
    |---|---|---|
    | **H** | I/J | K |
    | N | O   | P |
    | U | V   | **W** |
    
    **hw** => **KU**
    <br> 

Tekst podzielony na pary (diagram): **po-li-te-ch-ni-ka-po-zn-an-sk-ax**

Tekst zaszyfrowany (kryptogram): **QP-GK-XA-BI-OH-GD-QP-BU-BM-FG-ET**

Adresat znający słowo-klucz jest w stanie odwrócić procedurę ujawniając wiadomość.

---
## Algorytm kodujący
(TODO)

---
## Algorytm dekodujący
(TODO)
