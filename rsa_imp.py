import math
import random
from utils import generate_prime,mod_inverse

class rsa_imp:
    def __init__(self):
        self.public_key:int = None
        self.private_key:int = None
        self.p,self.q = generate_prime(1000,10000), generate_prime(1000,10000)
        while self.p == self.q:
            self.q = generate_prime(1000,10000)
        self.n = self.p*self.q
        self.phi_n = (self.p-1)*(self.q-1)

    def generateKeys(self):
        self.public_key= random.randint(3,self.phi_n-1)
        while math.gcd(self.public_key,self.phi_n) !=1:
           self.public_key= random.randint(3,self.phi_n-1)

        self.private_key= mod_inverse(self.public_key,self.phi_n)
        return self.public_key

    def encrypt(self,message:str,p_key:int):
        message_encoded = [ord(c) for c in message]

        ciphertext =  [pow(c,p_key,self.n) for c in message_encoded]
        return ciphertext
    
    def decrypt(self,ciphertext:list):
        message_encoded = [pow(c,self.private_key,self.n) for c in ciphertext]
        message_decrypted = "".join(chr(c) for c in message_encoded)    
        return message_decrypted
 

myRSA = rsa_imp()
myRSA.generateKeys()

print(myRSA.public_key)

print(myRSA.private_key,myRSA.public_key)

ciphertext = myRSA.encrypt('mensaje super secreto',myRSA.public_key)
print(ciphertext)

message = myRSA.decrypt(ciphertext)
print(message)

# print(f"public key: {e}")
# print(f"private key: {d}")
# print(f"n: {n}")
# print(f"phi: {phi_n}")
# print(f"p: {p}")
# print(f"q: {q}")

# message = 'This message is super secret'

# message_encoded = [ord(c) for c in message]

# # (m^e) mod n = c
# ciphertext =  [pow(c,e,n) for c in message_encoded]

# print(ciphertext)

# message_encoded = [pow(c,d,n) for c in ciphertext]

# message_decoded = "".join(chr(c) for c in message_encoded)

# print(message_decoded)