import math
import random
from utils.math_utils import generate_prime,mod_inverse,mcd

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
        while mcd(self.public_key,self.phi_n) !=1:
           self.public_key= random.randint(3,self.phi_n-1)

        self.private_key= mod_inverse(self.public_key,self.phi_n)
        return self.public_key

    def encrypt(self,message:str,p_key:int,n:int=None)->str: 
        message_encoded = [ord(c) for c in message]
        ciphertext =  [pow(c,p_key,n) for c in message_encoded]
        chipertext_string = "␟".join(str(cipher) for cipher in ciphertext)
        return chipertext_string
    
    def decrypt(self,ciphertext:str)->str:
        cipherlist = ciphertext.split("␟")
        message_prepared = [int(cipher) for cipher in cipherlist]
        message_encoded = [pow(c,self.private_key,self.n) for c in message_prepared]
        message_decrypted = "".join(chr(c) for c in message_encoded)    
        return message_decrypted
    
 
# myrsa = rsa_imp()

# myrsa.generateKeys()

# message = 'Sleeping is the best'

# ciphertext = myrsa.encrypt(message,myrsa.public_key,myrsa.n)

# print(ciphertext)

# decrypted = myrsa.decrypt(ciphertext)

# print(decrypted)