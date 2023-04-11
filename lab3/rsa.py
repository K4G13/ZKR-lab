from sympy import randprime

def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)

class rsa:

    def generate(self,range_s = 10**3,range_e = 10**4):
        p = randprime(range_s ,range_e)
        q = randprime(range_s ,range_e)
        n = p*q
        phi = (p-1)*(q-1)

        print(f"p = {p}")
        print(f"q = {q}")
        print(f"n = \033[93m{n}\033[0m")
        print(f"Φ = {phi}")

        e = None
        d = None
        while True:
            e = randprime(1, phi)
            d = pow(e,-1,phi)
            if gcd(e, phi) == 1 and e != d:
            # if e != d:
                break

        print(f"e = \033[93m{e}\033[0m")
        print(f"d = \033[93m{d}\033[0m")

        # Returns PUBLIC_KEY and PRIVATE_KEY
        return ((e,n),(d,n))
    
    def encrypt(self,public_key,msg):
        e,n = public_key
        code = []
        for i in msg:
            code.append(pow(ord(i), e, n))
        return code
    
    def decrypt(self,private_key,code):
        d,n = private_key
        msg = []
        for i in code:
            msg.append( chr(pow(i, d, n)) )
        return msg


RSA = rsa()
public,private = RSA.generate()

msg = "Rivest-Shamir-Adleman"
print(f" Original message: \033[93m{msg}\033[0m")

code = RSA.encrypt(public,msg)
print(f"Encrypted message: \033[91m{code}\033[0m")

msg_2 = ''.join( RSA.decrypt(private,code) )
print(f"Decrypted message: \033[92m{msg_2}\033[0m")