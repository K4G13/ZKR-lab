# Funkcje skrótu (haszujące)

## 2. Implementacja
biblioteka hashlib

## 3. Rola soli w tworzeniu skrutów
Sól pozwala zwiększyć siłę bezpieczeństwa funkcji skrótu w niektórych przypadkach. Sól może być losowa i dodawana automatycznie przez oprogramowanie do funkcji skrótu.  Jako że przechowywana jest jawnie, nie chroni przed atakami takimi jak Brute-Force, natomiast chroni przed atakami słownikowymi.

## 4. Czy funkcję MD5 można uznać	za	bezpieczną?	Czy	dotychczas	zostały	znalezione	dla	niej	jakiekolwiek	kolizje?
Dla	wybranej	przez	si
Problemy z algorytmem MD5 były znane już wcześniej. Funkcja ta, wynaleziona w 1991 r., generuje skrót o długości 128 bitów. To zbyt mało, by oprzeć się technikom kryptoanalizy dostępnym współcześnie. W związku z tym od kilku lat wśród producentów systemów kryptograficznych obserwuje się tendencję do odchodzenia od MD5 na rzecz SHA-1, dającego skrót 160-bitowy i będącego do niedawna standardem zalecanym przez Amerykański Instytut Standardów i Technologii (NIST).

W marcu 2005 Arjen Lenstra, Xiaoyun Wang i Benne de Weger zaprezentowali metodę umożliwiającą znalezienie kolizji dla algorytmu MD5 i przeprowadzenie ataku polegającego na wysłaniu dwóch różnych wiadomości chronionych tym samym podpisem cyfrowym. Kilka dni później Vlastimil Klima opublikował algorytm, który potrafił znaleźć kolizję w ciągu minuty, używając metody nazwanej tunneling.

https://pl.wikipedia.org/wiki/MD5

## 5. Wyniki pomiarów (1,000,000 losowych słów długości 10-255) i omówienie
|Name:       |Time[ms]:               |Hash length:            |Change %:               |
|:---:|---|:---:|:---:|
|sha1        |581.5002918243408       |40                      |46.88                   |
|md5         |603.4343242645264       |32                      |49.22                   |
|sha384      |622.3437786102295       |96                      |49.48                   |
|sha512      |625.298261642456        |128                     |48.83                   |
|sha224      |714.7369384765625       |56                      |48.66                   |
|sha256      |717.0226573944092       |64                      |53.12                   |
|sha3_224    |717.2260284423828       |56                      |50.45                   |
|sha3_256    |743.1461811065674       |64                      |50.78                   |
|sha3_384    |846.8992710113525       |96                      |50.78                   |
|sha3_512    |1067.3165321350098      |128                     |50.78                   |

Najszybszą funkcją skrótu są sha1 oraz md5.

Najbezpieczniejszą funkcją skrótu są sha3_512, sha512.