# Algorytm Rivesta-Shamira-Adlemana (RSA)
## Generowanie kluczy 🔐
1. Wbieramy dwie liczby pierwsze: **p** =31 oraz **q** =19
2. Obliczamy **n=p∙q** =589
3. Obliczamy **Φ=(p-1)(q-1)** =540
4. Generujemy **e** =7 gdzie: <br>
    a. **e** jest liczbą pierwszą <br>
    b. **1<e<Φ** 
5. Generujemy **d** =463 gdzie:<br>
    a. **d ≠ e**<br>
    b. **(e∙d - 1)mod(Φ) = 0**

**klucz publiczny: (e,n)** =(7,589)  
**klucz prywatny: (d,n)** =(463,589)

## Szyfrowanie 🔒
**c = m^e mod n**
gdzie **m** to wiadmość oryginalna a **c** wiadmość zaszyfrowana
np.
m = 8
c = 8^7 mod 589 = 312

## Deszyfrowanie 🔑
**m = c^d mod n**
gdzie **c** to wiadmość zaszyfrowana a **m** wiadmość oryginalna
np.
c = 312
c = 312^463 mod 589 = 8
___
# Algorytm	Diffiego-Hellmana (D-H)
## Krok 1 (👳🏾‍♂️👨🏻‍🦰):
Generujemy losową dużą liczbę pierwszą **n**.
Znajdujemy **g**, czyli pierwiastek pierwotny modulo **n** dla **1<g<n**.
Aktorzy **A**(👳🏾‍♂️) oraz **B**(👨🏻‍🦰) robią to w sposób jawny dla siebie nawzajem.
## Krok 2 (👳🏾‍♂️):
Aktor **A** wybiera dużą liczbę całkowitą **x**(tajną), która będzie jego kluczem prywatnym.
Oblicza on rónież **X = (g^x)mod(n)**.
## Krok 3 (👨🏻‍🦰):
Aktor **B** również wybiera dużą liczbę całkowitą **y**(tajną), która będzie jego kluczem prywatnym.
Oraz oblicza **Y = (g^y)mod(n)**.
## Krok 4 (👳🏾‍♂️👨🏻‍🦰):
Aktorzy **A** i **B** wymieniają się nawzajem **X** i **Y**.
👳🏾‍♂️🤝🏻👨🏻‍🦰
## Krok 5 (👳🏾‍♂️):
Aktor **A** oblicza **k = (Y^x)mod(n)**.
## Krok 6 (👨🏻‍🦰):
Aktor **B** oblicza **k = (X^y)mod(n)**.
## Krok 7 (👳🏾‍♂️👨🏻‍🦰):
Od teraz aktorzy **A** i **B** mogą używać **k** jako klucza sesji.