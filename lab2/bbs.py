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
    x = 0
    bitArray = []

    def set_p(self):
        self.p = random.randint(1000,9999)
        while isGoodPrime(self.p) == False:
            self.p = random.randint(1000,9999)
    
    def set_q(self):
        self.q = random.randint(1000,9999)
        while isGoodPrime(self.q) == False or self.q == self.p:
            self.q = random.randint(1000,9999)

    def set_x(self):        
        self.x = random.randint(1000,9999)
        while isPrime(self.x) == False or self.x == self.p or self.x == self.q:
            self.x = random.randint(1000,9999)

    def __init__(self):
        self.set_p()
        self.set_q()        
        self.set_x()

    def __init__(self,p,q):
        if p != q and isGoodPrime(p) and isGoodPrime(q):
            self.p = p
            self.q = q
        else:
            self.set_p()
            self.set_q()        
        self.set_x()
    
    def generate(self):
        n = self.p*self.q
        x0 = (self.x**2)%n

        X = []
        X.append(x0)
        for i in range(1,20000):
            X.append((X[i-1]**2)%n)

        for el in X:
            self.bitArray.append(el%2)

        return self.bitArray

      