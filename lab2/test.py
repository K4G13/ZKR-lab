#log colors
class lc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    G = '\033[92m' #Green
    Y = '\033[93m' #Yellow
    R = '\033[91m' #Red
    N = '\033[0m' #Normal
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


import bbs

p,q,n,x0,X,bitArray = bbs.generate()

#Test pojedynczych bitów
def test1():
    amount = 0
    for el in bitArray:
        if el == 1: amount+=1
    
    # print(amount)

    if 9725 < amount < 10275: return True
    else: return False

print(p,q,n)

if test1(): print("test1: Positive")
else: print("test1: Negative")