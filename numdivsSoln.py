
def factor(n):
    #n = p*q  
	#some p is a factor of n if n%p==0.
    #q=n//2
 #testing odds and evens
    
    if n%2==0:
        p=2 #
        q=n//2 #q is at least 1 so pq>1
    else: 
        i=3    #testing odd numbers
        
        while (i <= n) and (n%i!=0):     #shows there does not exist a common factor of i and n. so adding 2 to the value of i will make it an even number thus make it a common factor. since any multiple of 2 will have 2 as a factor.
            i+=2
        p=i
        q=n//i  #use same idea from testing p=2
    return(p,q)
     
            
   

    
       
    
    
    # Your code here. Find p and q with p,q > 1 and pq = n.
    # The order of p and q does not matter (e.g. if n=35, either 3,5 or 5,3 will be accepted)
  

