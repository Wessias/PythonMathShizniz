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





#Find the longest sequence of the digits fron 0 to 9, and the interval of the sequence.
#Maybe this formating for function names looks cleaner dno.
def longest_seq_in_list (DigList):
    
    digSequenceTracker = []
    
    tempSeqLength = 1
    tempSeqStart = 0
    tempSeqEnd = 0
    
    for i in range(0, 10):
        digSequenceTracker.append([i, 0, [0,0] ]) #Create list with 3 objects, digit, digit sequence length, sequence interval
                                                  
                                                  
    #First term manual ezpz, why did I do it so far away from the rest???                                                    Remains a mystery                             
    tempDig = DigList[0]
    
    for i in range(1, len(DigList)):
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
                
    #Doing last element update manually to fix problem of not updating freqList after last iteration in loop
    #I'm sorry programming gods for checking the same statement twice : (
    #                          Putting a -2 in here just did not wanna work in Python : ) Thanks Obama.
    if (DigList[-1] == DigList[len(DigList) - 2] and tempSeqLength > digSequenceTracker[DigList[-1]][1]):                
        
        tempSeqEnd = len(DigList) - 1 #Last index
        digSequenceTracker[DigList[-1]][1] = tempSeqLength #I don't use tempDig here cause it would be wrong if the last iteration of the for loop went through to the else statement
        digSequenceTracker[DigList[-1]][2][0] = tempSeqStart
        digSequenceTracker[DigList[-1]][2][1] = tempSeqEnd
        
    #I mean its def gonna be a seq with length 1 but it could be the longest ya never know
    elif (1 > digSequenceTracker[DigList[-1]][1]):
        digSequenceTracker[DigList[-1]][1] = 1
        digSequenceTracker[DigList[-1]][2][0] = len(DigList) - 1
        digSequenceTracker[DigList[-1]][2][1] = len(DigList) - 1
        
    
    
        
    return digSequenceTracker #Why is this the only one with sequence instead of seq? Retardation


 
digSeqOfPaj = longest_seq_in_list(np.int16(pi5)) #DOUBLE CHECK INDEX
DigSeqofE = longest_seq_in_list(np.int16(e5))

#a = longest_seq_in_list(tal1)
#b = longest_seq_in_list(tal2) 
#c = longest_seq_in_list(tal3)
#d = longest_seq_in_list(tal4)








#UPPGIFT 3
#Idno how to do this somewhat pretty :(




def seq_lengths_in_list(coolSeq):
    
    seqLengthTracker = [[1,0]] #OMG can this guy stop using LISTS? Yes, but no. The manual object is there so my for loop doesn't get insta error'd 
    
    tempDigerido = coolSeq[0]
    tempSeqLen = 0 #Spicing it up this time
    
    
    for coolDig in coolSeq:
        if (coolDig == tempDigerido):
            tempSeqLen += 1
            
            #Oh shit now we gotta add it to the tracker list bruh
        else:
            doesCurSeqLengthExistInList = False #Names are my specialty
            tempDigerido = coolDig
            
            #Why not i? D:
            for e in range(0, len(seqLengthTracker)):
                if (seqLengthTracker[e][0] == tempSeqLen):
                    seqLengthTracker[e][1] += 1
                    doesCurSeqLengthExistInList = True
                    
            if (not doesCurSeqLengthExistInList):
                seqLengthTracker.append([tempSeqLen, 1])
            tempSeqLen = 1
                
            
    #SAME SHIT AS EARLIER UPDATE TRACKER AFTER LAST ELEMENT
    if (coolSeq[-1] == coolSeq[len(coolSeq) - 2]):
        doesCurSeqLengthExistInList = False
        for e in range(0, len(seqLengthTracker)):
            if (seqLengthTracker[e][0] == tempSeqLen):
                seqLengthTracker[e][1] += 1
                doesCurSeqLengthExistInList = True
                
        if (not doesCurSeqLengthExistInList):
            seqLengthTracker.append([tempSeqLen, 1])
    
    #If the last ele isn't a part of the last sequence it's a lonely 1 length sequence
    else:
        seqLengthTracker[0][1] += 1
        
        
        #I make digSequenceTracker prettier. Why not do this for all of them so you don't forget what the numbers mean?! I don't need to know what the numbers mean Mason.
    for e in seqLengthTracker:
        e[0] = "Length " + str(e[0])
                
    return seqLengthTracker




A = seq_lengths_in_list(tal1)
B = seq_lengths_in_list(tal2)
C = seq_lengths_in_list(tal3)
D = seq_lengths_in_list(tal4)












