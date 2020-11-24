#Write a function crtList(ls) that takes a list ls of pairs (ai, mi) of integers, with any two of the values mi relatively prime, and returns a pair (a, m) such that the system of congruences x≡ai (modmi)isequivalentthesinglecongruencex≡a (modm),and0≤a<m(i.e. a is reduced modulo m).
def crtList(ls):
    #try to separate pairs? cause idk how to do it otherwise.
    ai = [x[0] for x in ls]
    mi = [x[1] for x in ls]
    #if you separate pairs into lists then it might be easier, for me haha, to do any operations with them. lets focus on a's and m's separately. probably not doing these lists the way you want me to but i'm using a method from a data science python tutorial instead
    
    while len(ai) > 2:
        q_temp = (((ai[1]-ai[0])%mi[1])*(modinv(mi[0],mi[1])))%mi[1]
        ai_temp = (ai[0]+mi[0]*q_temp)%(mi[0]*mi[1])
        mi_temp = mi[0]*mi[1]
        ai.remove(ai[0])
        ai.remove(ai[0])
        ai.append(ai_temp)        #using these to place temporary values. Essentially the EEA for lists. Assigning temporary variable and them reevaluating them for the next term in the list. sort of. 
        m_temp = mi[0]*mi[1]
        mi.append(mi_temp)
        mi.remove(mi[0])
        mi.remove(mi[0])
        
                 
        if len(ai) == 2:
            break
    q = (((ai[1]-ai[0])%mi[1])*(modinv(mi[0],mi[1])))%mi[1]
    a = (ai[0]+mi[0]*q)%(mi[0]*mi[1])
    m =  mi[0]*mi[1]
    
    return [a,m]
           

         #basic crt forumla 
   
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
   

