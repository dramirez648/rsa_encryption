##Daniel Ramirez
##RSA Encryption/Decryption & Key Generator

import random
from fractions import gcd

def rsa():
    x = int(eval(input("Enter plaintext integer: ")))

    primes = [i for i in range(32768, 65535) if isPrime(i)]
    
    ap = random.choice(primes)

    aq = random.choice(primes)
        
    an = (ap) * (aq)
    
    aphin = (ap-1) * (aq-1)
    
    ae = random.randint(32768, 65535)
    while (gcd(ae, aphin) != 1):
        ae = random.randint(32768, 65535)
    ad = modinv(ae, aphin)

    bp = random.choice(primes)

    bq = random.choice(primes)

    bn = (bp) * (bq)
    
    bphin = (bp-1) * (bq-1)
    
    be = random.randint(32768, 65535)
    while (gcd(be, bphin) != 1):
        be = random.randint(32768, 65535)
    bd = modinv(be, bphin)

    print("x = " + str(x))
    print("Alicia's keys: ")
    print("p = " + str(ap))
    print("q = " + str(aq))
    print("n = " + str(an))
    print("e = " + str(ae))
    print("d = " + str(ad))
    
    print("Bob's keys: ")
    print("p = " + str(bp))
    print("q = " + str(bq))
    print("n = " + str(bn))
    print("e = " + str(be))
    print("d = " + str(bd))

    print("Signing x")
    s = mod_pow(x, ad, an)
    print("s = " + str(s))

    print("Encrypting x ")
    y = mod_pow(x, ae, an)
    print("y = " + str(y))

    decrypt = mod_pow(y, ad, an)
    print("Decrypted y (x) = " + str(decrypt))

    print("Signature verification (x) = " + str(mod_pow(s, ae, an)))

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):  
        if n%i==0:
            return False    

    return True

def mod_pow(base, exponent, modulus):
    result = 1;

    while (exponent > 0):
        if (exponent % 2 == 1):
           result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
    
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
      
    
