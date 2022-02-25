# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:04:12 2022

@author: Regnd
"""
import numpy as np

class Quaternion():
    def __init__(self, a,b,c,d):
        self.r = a
        self.i = b
        self.j = c
        self.k = d

        

def qadd(q1,q2):
    
     return Quaternion( (q1.r + q2.r), (q1.i + q2.i), (q1.j + q2.j) , (q1.k + q2.k) )
 

def qsub(q1,q2):
    
    return Quaternion( (q1.r - q2.r), (q1.i - q2.i), (q1.j - q2.j) , (q1.k - q2.k) )
     

def qmul(q1,q2):
    
    r = q1.r * q2.r - q1.i * q2.i - q1.j * q2.j - q1.k * q2.k
    print(r)
    i = q1.r * q2.i + q1.i * q2.r + q1.j * q2.k - q1.k * q2.j
    j = q1.r * q2.j - q1.i * q2.k + q1.j * q2.r + q1.k * q2.i
    k = q1.r * q2.k + q1.i * q2.j - q1.j * q2.i + q1.k * q2.r
    
    return Quaternion(r,i,j,k)


def qdiv(q1,q2):
    return qmul(q1,qinv(q2))
    

def sclrmul(q1, s):
    q1.r *= s
    q1.i *= s
    q1.j *= s
    q1.k *= s
    return q1
    

def qabs(q1):
    return (np.sqrt(q1.r**2 + q1.i**2 + q1.j**2 + q1.k**2 ))

def qconj(q1):
    i = q1.i * -1
    j = q1.j * -1
    k = q1.k * -1
    return qcons(q1.r,i,j,k)

def qcons(a,b,c,d):
    return Quaternion(a,b,c,d)

def qinv(q1):
    q = qconj(q1)
    qInv = sclrmul(q,1/(qabs(q1)**2)) 
    return qInv



def qprint(q):
    print("(" + str(q.r) + ",", str(q.i) + ",", str(q.j) + ",", str(q.k) + ")")
    
def qread():
    qL = []
    for i in range(1,5):
        ipt = input("Enter a" + str(i) + " ")
        qL.append(float(ipt))
    
    return qcons(qL[0], qL[1], qL[2], qL[3])        