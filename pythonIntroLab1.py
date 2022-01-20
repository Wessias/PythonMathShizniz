# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 14:48:31 2022

@author: 
    
"""
import math
from random import random 
pi = math.pi




#UPPGIFT 1: APPROXIMERA PI

# n = shots
def approxPi(n):
    onCircle = 0
    for i in range(0, n):
        x = random()
        y = random()   
        
        if( (x - 1/2)**2 + (y - 1/2)**2 <= 1/4):
            onCircle += 1
            
    PiApprox = (onCircle / n) * 4
    return PiApprox
    
#x = approxPi(696969)
#print("Approx of pi is", x,"\nDeviation from pi is", abs(x-pi))

#-----------------------------------------------------------------------------

#UPPGIFT 2: APPROXIMERA INTEGRAL
#INTEGRALEN: (1-x^3)^(1/3)

def approxInt(n, f):
    belowFunc = 0
    for i in range(0, n):
        x = random()
        y = random()
        
        if(y <= f(x)):
            belowFunc += 1
            
    approxInt = belowFunc / n
    return approxInt

f = lambda x : (1-x**3)**(1/3)

#I = approxInt(420420, f)



#-----------------------------------------------------------------------------


#UPPGIFT 3: RATIONELL APPROX AV PI


startApprox = 355/113

# c = value that should be approximated
def betterRationalApprox(valueToApprox, curApprox, startQ):
    q = startQ
    p = q * math.floor(valueToApprox)
    while(True):
        
        if (p/q >= valueToApprox + abs(curApprox - valueToApprox)):
            q += 1
            p = q * math.floor(valueToApprox)

        elif(abs( p/q - valueToApprox) < abs(curApprox - valueToApprox)):
            return (p,q)
        else:
            p += 1

    
    
#B = betterRationalApprox(pi, startApprox, 99531)
#print(B, "in the form (p,q)")


def econRationalApprox(valueToApprox, curApprox, digits):
    q = 1
    p = q * math.floor(valueToApprox)
    bestP = 1
    bestQ = 1 * 10**(digits-1)
    while(True):
        
        if (len(str(q)) > digits):
          return (bestP,bestQ)  
          
        elif (p/q >= valueToApprox + abs(curApprox - valueToApprox)):
            q += 1
            p = q * math.floor(valueToApprox)
            
            
        elif(abs( p/q - valueToApprox) < abs(curApprox - valueToApprox)):
            bestP = p
            bestQ = q
            curApprox = p/q
        
        else:
            p += 1
            

for i in range(1, 5):
    
    RationalNum = econRationalApprox(math.e, 2.7,i)
    print(RationalNum[0], "/", RationalNum[1], "is the best economical approximation with", i, "digits in the denominator" )
    curBestApprox = RationalNum[0] / RationalNum[1]




e_frac = [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12]

def approx(fracExpanse, exact):
    # initialize the recurrence http://oeis.org/A003417
    n0 = fracExpanse[0]
    d0 = 1
    n1 = fracExpanse[0]*fracExpanse[1] + 1
    d1 = fracExpanse[1]

    print(n0, d0)
    print(n1, d1)

    for x in fracExpanse[2:]:
        n = x*n1 + n0 # numerator
        d = x*d1 + d0 # denominator
        print (n, d, n/d)
        n1, n0 = n, n1
        d1, d0 = d, d1

approx(e_frac, math.e)


































