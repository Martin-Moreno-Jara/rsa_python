import random 

def mod_inverse(e,phi):
    for d in range(3,phi):
        if(d*e)%phi == 1:
            return d 
    raise ValueError("No existe el inverso modular")
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