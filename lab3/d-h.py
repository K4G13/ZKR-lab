from sympy import randprime
import random

def primitiveRoots(p,max_amount=0):
    
    primitive_roots = []

    for g in range(2,p):
        print(f"Testing {g}^k mod({p}) ... ")
        array = []
        for k in range(1,p): 
            array.append(pow(g,k,p))           
        if len([*set(array)]) == p-1:
            primitive_roots.append(g)
            if max_amount!=0 and len(primitive_roots)>=max_amount:
                return primitive_roots 
    
    return primitive_roots  

#step 1 AB
n = randprime(10**5,10**6)
print("n:\t",n)
g = primitiveRoots(n,1)[-1]
print("g:\t",g)

#step 2 A
### A's private key:
x = random.randint(2**1024,2**2048)
print("x:\t",x)
X = pow(g,x,n)
print("X:\t",X)

#step 3 B
### B's private key:
y = random.randint(2**1024,2**2048)
print("y:\t",y)
Y = pow(g,y,n)
print("Y:\t",Y)

#step 4 AB
# A and B send each otrher X and Y

#step 5 A
k_a = pow(Y,x,n)
print("k_a:\t",k_a)

#step 6 B
k_b = pow(Y,x,n)
print("k_b:\t",k_b)