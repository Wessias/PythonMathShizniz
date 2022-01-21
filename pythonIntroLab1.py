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
    
x = approxPi(696969)
print("Approx of pi is", x,"\nDeviation from pi is", abs(x-pi))

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

I = approxInt(math.factorial(10), f)



#-----------------------------------------------------------------------------


#UPPGIFT 3: RATIONELL APPROX AV PI


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

    
    
B = betterRationalApprox(pi, 355/113, 113)
print(B, "in the form (p,q) is the next best rational approximation p/q of pi after 355/113")






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
            

#for i in range(1, 5):
#    
#    RationalNum = econRationalApprox(math.e, 2.7,i)
#    print(RationalNum[0], "/", RationalNum[1], "is the best economical approximation with", i, "digits in the denominator" )
#    curBestApprox = RationalNum[0] / RationalNum[1]



#-----------------------------------------------------------------------------





#BÄTTRE UPPGIFT 3 OCH 4:


def fracRep(realNum, termsInFrac):
    
    frac = []
    
    for i in range(0, termsInFrac):
        n = math.floor(realNum)
        frac.append(n)
        realNum = 1 / (realNum - n)
        
    return frac

paj_frac = fracRep(pi, 42)    
e_frac = fracRep(math.e, 69)

#https://en.wikipedia.org/wiki/Continued_fraction#Continued_fraction_expansion_of_%CF%80_and_its_convergents
#http://oeis.org/A003417

def findBetterRatApprox(fracExpanse, numToApprox, curApprox):
    # initialize the recursion 
    p0 = fracExpanse[0]
    q0 = 1
    p1 = fracExpanse[0]*fracExpanse[1] + 1
    q1 = fracExpanse[1]

    for i in fracExpanse[2:]:
        p = i*p1 + p0 # numerator
        q = i*q1 + q0 # denominator
        if ( abs(p / q - numToApprox) < abs(curApprox - numToApprox) ):
            return (p,q)
        p1, p0 = p, p1
        q1, q0 = q, q1

pajApprox = findBetterRatApprox(paj_frac, pi, 355/113)



def findEconRatApprox(fracExpanse, numToApprox, digitsOfQ):
    
    p0 = fracExpanse[0]
    q0 = 1
    p1 = fracExpanse[0]*fracExpanse[1] + 1
    q1 = fracExpanse[1]
    tempP = 0
    tempQ = 1
    for i in fracExpanse[2:]:
        p = i*p1 + p0 # numerator
        q = i*q1 + q0 # denominator
        if ( len(str(q)) > digitsOfQ ):
            return (tempP, tempQ)
        
        elif (abs(p / q - numToApprox) < abs(tempP / tempQ - numToApprox)):
            tempP = p
            tempQ = q
            
        p1, p0 = p, p1
        q1, q0 = q, q1


econRats = []
for i in range(1, 7):
    econRats.append(findEconRatApprox(e_frac, math.e, i))
    print("Best rational approximation of e with", i, "digit(s) in the denominator is", econRats[i - 1])



























