#Devise a method to create “blind forgeries” for a given DSA public key. That is, write a function dsaBlind(p,q,g,A) given p, g and A as in DSA, generate integers (d, s1, s2) such that (s1, s2) is a valid signature for d for the verification key A. You will likely want to adapt the strategy from one of last weeek’s problems from Elgamal to DSA. Your method should be non-deterministic; the grading script will give the same test case multiple times to check that the same answer is not returned each time.
import random
import math
def dsaBlind(p,q,g,A):
    i = random.randint(1,q)%q
    j = 1
    while math.gcd(j,p-1)!= 1:
        j+=1
    s1 = ((pow(g,i,p)*pow(A,j,p))%p)%q
    s2 = linearCong(j,s1,q)
    d = linearCong(j,s1*i,q)
    return d,s1,s2

def modinv(a,b): 
    r0 = a
    r1 = b
    u0 = 1
    v0 = 0
    u1 = 0
    v1 = 1
    while r1!=0:
      q = r0 // r1
      r2 = r0-q*r1  
      u2 = u0-q*u1
      v2 = v0-q*v1
      u0 = u1
      v0 = v1
      u1 = u2
      v1 = v2
      r0 = r1 
      r1 = r2
    return u0
def bezout(a,b): 
   r0 = a
   r1 = b
   u0 = 1
   v0 = 0
   u1 = 0
   v1 = 1
   while r0%r1!=0:
      q = r0 // r1
      r2 = r0%r1  
      u2 = u0-q*u1
      v2 = v0-q*v1
      u0 = u1
      v0 = v1
      u1 = u2
      v1 = v2
      r0 = r1 
      r1 = r2
   return r1, u1, v1
 
   
def linearCong(m,b,N):
    
    lst = bezout(m,N)
    if lst[0] == 1:
        j = (b * modinv(m,N)) % N
        M = N
        return j
    if lst[0] != 1:
        m1 = m // lst[0]
        b1 = b // lst[0]
        N1 = N // lst[0]
        
        #if b_new.is_integer()==False:
            #return None
        
        lst2 = bezout(m1,N1)
        
        
        if lst2[0] != 1:
            return None
        
        if lst2[0] == 1: 
            j = (b1 * modinv(m1,N1)) % N1
            M = N1
           
            return j
        
        return j
   



