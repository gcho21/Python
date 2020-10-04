#Write a function verifyDSA(p,q,g,A,d,s1,s2) that verifies DSA signatures. Here, p,q,g are public parameters, A is the public (verification) key, d is the document, and (s1, s2) is the signature. The function should return True or False.

def verifyDSA(p,q,g,A,d,s1,s2):
    x = modinv(s2,q)
    v1 = (d*x)%q
    v2 = (s1*x)%q

    if ((pow(g,v1,p) * pow(A,v2,p))%p)%q == s1:
        return True
    else:
        return False
    
  
   
    
    
    
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
   