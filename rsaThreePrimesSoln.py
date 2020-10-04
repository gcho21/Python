# Alice decides that she wants to receive messages using a non-standard variant of RSA. Like in the usual RSA, she will choose a public key N, e, where N is a number whose factorization she knows, and gcd(e, φ(N )) = 1. In this case, she will take N = pqr, where p, q, r are distinct primes. To encrypt a message m for Alice (0 ≤ m < N), Bob computes c ≡ me (mod N). Write a function rsaThreePrimes(p,q,r,e,c) to do the following: given the three primes p, q, r, the number e, and the ciphertext c sent by Bob, recover the original plaintext m.
#Note. While this setup is perfectly functional, in practice it is more efficient to use products of two primes, hence that is the standard. I encourage you to think about why it is more efficient to use only two primes.
def rsaThreePrimes(p,q,r,e,c):
    N = p*q*r
    N1 = (p-1)*(q-1)*(r-1)
    d = modinv(e,N1)
    
    if d >= 1:
        k = pow(c,d,N)
    
    else: 
        D = -1*d
        cinv = modinv(c,N)
        k = pow(cinv,D,N)
    
    return k


    



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
