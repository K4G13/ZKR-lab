# Algorytm
1. wyznaczamy wartość iloczynu **n** dwóch dużych liczb	pierwszych,	takich że:
    - **p** mod 4 = 3
    - **q** mod 4 = 3
2. wybieramy w sposób losowy taką liczbę **x**, że **x** i **n** są wzglęnie pierwsze
3. wyznaczamy wartość **x0**(pierwotną/seed) generatora:
    - **x0** = x² mod n
4. powtarzamy w pętli: 
    - **x(i+1)** = x(i)² mod n 