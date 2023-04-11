# RSA
p i q przynajmniej 2048 bitów do 4096
phi(n) = phi(p)*phi(q) = (p-1)(q-1)
e - losowa liczba  e,phi(n) nie maja wspólnych dzielników
d - odwrotność liczby e    d*e = 1 mod phi(n)
d = pow(e,-1,phi(n)) <- w pythonie

SZYFROWANINE:
m^e mod n = c
A  L  A     M  A  ...   zamienić na ascii(?)
c1 c2 c3 c4 c5 c6 ...

# DH
primitive root 