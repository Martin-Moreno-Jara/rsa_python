import random 

def mcd(a:int,b:int):
    if a == 0 and b == 0:
        raise ValueError('No existe MCD')
    if b == 0:
        return a
    else:
       return mcd(b,a%b)

def extended_mcd(a:int,b:int):
    if b==0:
        mcd,x,y = a,1,0
    else:
        (p,q,mcd) = extended_mcd(b,a%b)
        x=q
        y = p-q * (a//b)
    assert a % mcd == 0 and b % mcd == 0
    assert mcd == a*x + b*y
    return (x,y,mcd)

def mod_inverse(e,phi):
    if(mcd(phi,e) != 1):
        raise ValueError("No existe el inverso modular")
    x,_,_ = extended_mcd(e,phi)
    inverse = x % phi
    assert (e*inverse)%phi ==1
    return inverse

def min_divisor(m:int):
    for number in range (2,m+1):
        if m % number == 0:
            return number
        if number*number>m:
            return m
        

def is_prime(number:int):
    # if number<2:
    #     return False
    # for i in range(2,number//2+1):
    #     if number % i ==0:
    #         return False
    # return True
    return number == min_divisor(number)

def generate_prime(min_val:int,max_val:int):
    prime:int = random.randint(min_val,max_val)
    while not is_prime(prime):
        prime:int = random.randint(min_val,max_val)
    return prime