import random

def isPrime(n):
  for i in range(2,int(n/2)):
    if (n%i) == 0:
      return False
  return True

#examples for True val: 5443 2963 3323 6983
def isGoodPrime(n):
    if n%4==3 and isPrime(n): return True
    else: return False

def generate():
    p = random.randint(1000,9999)
    while isGoodPrime(p) == False:
        p = random.randint(1000,9999)

    q = random.randint(1000,9999)
    while isGoodPrime(q) == False or q == p:
        q = random.randint(1000,9999)

    n = p*q    

    x0 = random.randint(1000,9999)
    while isPrime(x0) == False or x0 == p or x0 == q:
        x0 = random.randint(1000,9999)
   
    X = []
    X.append(x0)
    for i in range(1,20000):
        X.append((X[i-1]**2)%n)

    bitArray = []
    for el in X:
        bitArray.append(el%2)

    return p,q,n,x0,X,bitArray