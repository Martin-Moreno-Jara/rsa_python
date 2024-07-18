import random 
import math

def is_prime(number:int):
    if number<2:
        return False
    for i in range(2,number//2+1):
        if number % i ==0:
            return False
    return True

def generate_prime(min_val:int,max_val:int):
    prime:int = random.randint(min_val,max_val)
    while not is_prime(prime):
        prime:int = random.randint(min_val,max_val)
    return prime

def mod_inverse(e,phi):
    for d in range(3,phi):
        if(d*e)%phi == 1:
            return d 
    raise ValueError("No existe el inverso modular")

p,q = generate_prime(1000,10000), generate_prime(1000,10000)

while p == q:
    q = generate_prime(1000,10000)

n = p*q

phi_n = (p-1)*(q-1)

e= random.randint(3,phi_n-1)

while math.gcd(e,phi_n) !=1:
    e= random.randint(3,phi_n-1)

d= mod_inverse(e,phi_n)

print(f"public key: {e}")
print(f"private key: {d}")
print(f"n: {n}")
print(f"phi: {phi_n}")
print(f"p: {p}")
print(f"q: {q}")

message = 'This message is super secret'

message_encoded = [ord(c) for c in message]

# (m^e) mod n = c
ciphertext =  [pow(c,e,n) for c in message_encoded]

print(ciphertext)

message_encoded = [pow(c,d,n) for c in ciphertext]

message_decoded = "".join(chr(c) for c in message_encoded)

print(message_decoded)