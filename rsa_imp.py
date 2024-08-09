import math
import random
from utils.math_utils import generate_prime,mod_inverse,mcd,mod_exp

class rsa_imp:
    def __init__(self):
        self.public_key:int = None
        self.private_key:int = None
        self.p,self.q = generate_prime(42), generate_prime(42)
        while self.p == self.q:
            self.q = generate_prime(42)
        self.n = self.p*self.q
        self.phi_n = (self.p-1)*(self.q-1)

    def generateKeys(self):
        keysize=42
        while True:
            self.public_key = random.randrange(2** (keysize-1),2 ** keysize -1)
            if mcd(self.public_key,self.phi_n) ==1:
                break
        
        #self.public_key= random.randint(3,self.phi_n-1)
        # while mcd(self.public_key,self.phi_n) !=1:
        #    self.public_key= random.randint(3,self.phi_n-1)

        self.private_key= mod_inverse(self.public_key,self.phi_n)
        return self.public_key

    def encrypt(self,message:str,p_key:int,n:int=None)->str: 
        message_encoded = [ord(c) for c in message]
        ciphertext =  [mod_exp(c,p_key,n) for c in message_encoded]
        chipertext_string = "␟".join(str(cipher) for cipher in ciphertext)
        return chipertext_string
    
    def decrypt(self,ciphertext:str)->str:
        cipherlist = ciphertext.split("␟")
        message_prepared = [int(cipher) for cipher in cipherlist]
        message_encoded = [mod_exp(c,self.private_key,self.n) for c in message_prepared]
        message_decrypted = "".join(chr(c) for c in message_encoded)    
        return message_decrypted
    
 
myrsa = rsa_imp()

myrsa.generateKeys()

print('keys ///')
print(myrsa.public_key)
print(myrsa.private_key)

message = 'Sleeping is the best'

ciphertext = myrsa.encrypt(message,myrsa.public_key,myrsa.n)

print(ciphertext)

decrypted = myrsa.decrypt(ciphertext)

print(decrypted)