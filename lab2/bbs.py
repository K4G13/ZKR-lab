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

class BBS:  

    p = 0
    q = 0
    x0 = 0
    bitArray = []

    def __init__(self):
        self.p = random.randint(1000,9999)
        while isGoodPrime(self.p) == False:
            self.p = random.randint(1000,9999)
        
        self.q = random.randint(1000,9999)
        while isGoodPrime(self.q) == False or self.q == self.p:
            self.q = random.randint(1000,9999)

        self.x0 = random.randint(1000,9999)
        while isPrime(self.x0) == False or self.x0 == self.p or self.x0 == self.q:
            self.x0 = random.randint(1000,9999)

    def generate(self):
        n = self.p*self.q

        X = []
        X.append(self.x0)
        for i in range(1,20000):
            X.append((X[i-1]**2)%n)

        for el in X:
            self.bitArray.append(el%2)

        return self.bitArray

      