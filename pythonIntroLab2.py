# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 16:19:13 2022

@author: Regnd
"""

import numpy as np

pi5 = np.load("pi5.npy")
e5 = np.load("e5.npy")

#UPPGIFT 1:
#Skriv en Pythonfunktion som kan användas till att räkna ut antalet gånger 
#siffrorna 0 till 9 förekommer i pi5 (eller e5). 
#Låt funktionen ha en inparameter, en vektor. 
#Det skall räcka att anropa funktionen en gång för att få ut alla resultat. 
#Man anropar lämpligen funktionen från ett huvudprogram som sköter utskrifter och liknande.



def freqOfSingDigitsInList(listToCheck):
    
    digFreqTracker = [] 
    for i in range(0, 10):
        digFreqTracker.append([i,0]) #Populate list with lists where the lists within are in the form (digit, digitCounter)
    
    for curDig in listToCheck:
        for i in range(0, 10):
            if (curDig == i):
                digFreqTracker[i][1] += 1
                break
            
       
        
       
    return digFreqTracker
        
        


#freq_e = freqOfSingDigitsInList(e5)
#freq_paj = freqOfSingDigitsInList(pi5)


#-----------------------------------------------------------------------------


#UPPGIFT 2

# vektorlängd ett, dessutom finns inte alla siffror med
tal1 = np.array([1]) 

# sekvensen avslutas med att vektorn "tar slut"                
tal2 = np.array([1, 1, 1, 1, 1])  

# här avslutas sekvensen med annan siffra   
tal3 = np.array([1, 1, 1, 1, 1, 2])  

# sekvenser av olika längder (med samma siffra), den längsta sekvensen kommer inte sist
tal4 = [2, 1, 1, 2, 3, 4, 1, 1, 1, 2, 2, 4, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 1, 1, 1]





#Find the longest sequence of a certain digit d and the interval of indexes of the sequence.
#Maybe this formating of functions looks cleaner dno.
def longest_seq_in_list (DigList):
    
    digSequenceTracker = []
    
    tempSeqLength = 1
    tempDig = 0 #Lets just make sure no sequence starts with 0 ;)
    tempSeqStart = 0
    tempSeqEnd = 0
    
    for i in range(0, 10):
        digSequenceTracker.append([i, 0, [0,0] ]) #Create list with 3 objects, digit, digit sequence length, sequence interval
                                                  #I just decided that if the interval is [0,0] then the digit has no sequence, sorry if you're a digit that only appears once at the start (can check with eyes)
                                                  #If 0 is neever in the sequence it will show up as [0, 1, [0, -1]] and I'm too lazy to care
    for i in range(0, len(DigList)):
            if (DigList[i] == tempDig):
                tempSeqLength += 1
                
            else:
                tempSeqEnd = i - 1 #If the ele at index i wasn't in the current seq the last one of the sequence must be ele at index (i - 1)
                
                if (tempSeqLength > digSequenceTracker[tempDig][1]):
                    digSequenceTracker[tempDig][1] = tempSeqLength #Update longest seq
                    digSequenceTracker[tempDig][2][0] = tempSeqStart #Update interval
                    digSequenceTracker[tempDig][2][1] = tempSeqEnd
                
                tempDig = DigList[i]
                tempSeqStart = i
                tempSeqLength = 1
                
        
        
        
        
    
    return digSequenceTracker


 
digSeqOfPaj = longest_seq_in_list(np.int16(pi5)) #DOUBLE CHECK INDEX
DigSeqofE = longest_seq_in_list(np.int16(e5))

a = longest_seq_in_list(tal1)
b = longest_seq_in_list(tal2) #LAST INDEX GETS FUGD, should prob do special for 1st and last
c = longest_seq_in_list(tal3)
d = longest_seq_in_list(tal4)


np.int
















