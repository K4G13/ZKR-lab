from sympy import randprime
import math

def nwd(a, b): return nwd(b, a%b) if b else a

class RSA:

    p = 0
    q = 0
    n = 0
    phi = 0
    e = 0
    d = 0   

    def __init__(self):
        self.p = randprime(1000,9999)
        self.q = randprime(1000,9999)
        self.n = self.p * self.q
        self.phi = (self.p - 1)*(self.q - 1)
        # self.e = randprime(1,self.phi)
        self.e = 2
        while(self.e<self.phi):
            if (math.gcd(self.e, self.phi) == 1):
                break
            else:
                self.e += 1
        self.d = pow(self.e,-1,self.phi)
        # k = 2
        # self.d = int(((k*self.phi)+1)/self.e)
        

    def encryption(self,m):
        c = (m**self.e)%(self.n)
        return c
    
    def decryption(self,c):
        m = (c**self.d)%(self.n)
        return m
    
    def encrypt(self,message):
        code = []
        for ch in message:
            code.append( self.encryption(ord(ch)) )
        return code
    
    def decrypt(self,code):
        message = ""
        for x in code:
            message += str( chr(self.decryption(x)) )
        return message


    def dev(self):
        print("n:   ",self.n)
        print("phi: ",self.phi)
        print("e:   ",self.e)
        print("d:   ",self.d)


rsa = RSA()

rsa.dev()

PLAIN_TEXT = "Politechnika Poznańska"
print(f"\033[93mPlain text:    \033[0m {PLAIN_TEXT}")

ENCRYPTED_TEXT = rsa.encrypt(PLAIN_TEXT)
print(f"\033[93mEncrypted text:\033[0m {ENCRYPTED_TEXT}")

DECRYPTED_TEXT = rsa.decrypt(ENCRYPTED_TEXT)
print(f"\033[91mDecrypted text:\033[0m {DECRYPTED_TEXT}")