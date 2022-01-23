# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:19:13 2022

@author: Regnd
"""

import numpy as np

pi5 = np.load("pi5.npy")
e5 = np.load("e5.npy")


#Skriv en Pythonfunktion som kan användas till att räkna ut antalet gånger 
#siffrorna 0 till 9 förekommer i pi5 (eller e5). 
#Låt funktionen ha en inparameter, en vektor. 
#Det skall räcka att anropa funktionen en gång för att få ut alla resultat. 
#Man anropar lämpligen funktionen från ett huvudprogram som sköter utskrifter och liknande.



def freqOfSingDigitsInList(listToCheck):
    
    digFreq = [] 
    for i in range(0, 10):
        digFreq.append([i,0])
    
    for curDig in listToCheck:
        for i in range(0, 10):
            if (curDig == i):
                digFreq[i][1] += 1
                break
            
       
        
       
    return digFreq
        
        


freq_e = freqOfSingDigitsInList(e5)
freq_paj = freqOfSingDigitsInList(pi5)