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
    r = q1.r*q2.r - q1.i*q2.i -  q1.j*q2.j - q1.k*q2.k
    i = q1.r*q2.i + q1.i * q2.r + q1.j*q2.k - q1.k*q2.j
    j = q1.r*q2.j - q1.i*q2.k + q1.j*q2.r + q1.k*q2.i
    k = q1.r*q2.k + q1.i*q2.j - q1.j*q2.i + q1.k&q2.r
    
    return Quaternion(r,i,j,k)
    