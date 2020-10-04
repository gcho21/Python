#Write a function dh(g,p,B) that performs Alice’s role in Diffie-Hellman key exchange, using a randomly chosen secret number a. More precisely: you are given a prime number p, an element g ∈ Z/pZ, and Bob’s transmission B. Your function should return a pair of two numbers A,S, where A is the number you transmit to Bob, and S is the shared secret. You should look up how to generate random numbers in Python (don’t worry about finding a “cryptographically secure” random number generator, just use the standard one in Python). The prime p will be between 16 and 256 bits long, and the autograder will run your code several times on each input to make sure that it appears to be choosing the secret number a randomly.
from random import randint
def dh(g,p,B):
        a = randint(2**3,2**8)
        A = pow(g,a,p)
        S = pow(B,a,p)
        return A,S
