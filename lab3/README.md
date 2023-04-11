# RSA
## Generowanie kluczy:
1) Wbieramy dwie liczby pierwsze: **p** =31 oraz **q** =19
2) Obliczamy **n=p∙q** =589
3) Obliczamy **Φ=(p-1)(q-1)** =540
4) Generujemy **e** =7 gdzie:
    1) **e** jest liczbą pierwszą
    2) **1<e<Φ**
5) Generujemy **d** =463 gdzie:
    a) **d ≠ e**
    b) **(e∙d - 1)mod(Φ) = 0**

**klucz publiczny: (e,n)** =(7,589)  
**klucz prywatny: (d,n)** =(463,589)

## Szyfrowanie:
**c = m^e mod n**
gdzie **m** to wiadmość oryginalna a **c** wiadmość zaszyfrowana
np.
m = 8
c = 8^7 mod 589 = 312

## Deszyfrowanie:
**m = c^d mod n**
gdzie **c** to wiadmość zaszyfrowana a **m** wiadmość oryginalna
np.
c = 312
c = 312^463 mod 589 = 8
___
# DH
primitive root 
