# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:46:45 2022

@author: Regnd
"""

testKey = "PLAYFAIREXAMPLE"


def populate_matrix_with_key(key, matrix):
    
    iCount = 0
    
    for row in matrix:
        for col in range(5):
            row[col] = key[iCount]
            iCount += 1
            if (iCount == len(key)):
                return matrix

  
#-----------------------------------------------------------------------------  


def create_n_matrix(n):
    M = []
    for row in range(n):
        tempList = []
        for col in range(n):
            tempList.append([""])
            
        M.append(tempList)
    return M

#-----------------------------------------------------------------------------

def poupulate_with_rest_of_alpha(key, Matrix):
    alpha = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
    for letter in key:
        alpha = alpha.replace(letter, "")
        
    print(alpha)
    
    lettersAdded = 0
    for row in Matrix:
        for col in range(5):
            if (row[col][0] == ""):
                row[col][0] = alpha[lettersAdded]
                lettersAdded = lettersAdded + 1
    
    
    print(lettersAdded)
    return Matrix

#-----------------------------------------------------------------------------


def list_of_split_string_in_pairs(text):
    tempText = ""
    
    for i in range(len(text) - 1): # -1 there to not fall out of index
        if (text[i] == text[i + 1] and i % 2 == 0):
            split = text[i]
            split += "X"
            tempText += split
        else:
            tempText += text[i]
            
    tempText += text[-1] #The last letter needs to join in on the fun too
    if(len(tempText) % 2 == 1):
        tempText += "X"

    
    listOfPairs = []
    
    for i in range(0, len(tempText), 2):
        listOfPairs.append(tempText[i:i + 2])
    
    return listOfPairs

Q = list_of_split_string_in_pairs("HIDETHEGOLDINTHETREESTUMP")

#-----------------------------------------------------------------------------


def playfair(text, key, crypt):
    
    
    sign = -1 # YOU SEE THIS VAR LATER IN CODE
    if(crypt): #If you you're decrypting the indexs will "move" left if you're encrypting they "move" right.
        sign = 1
    
    finKey = ""
    
    for letter in key:
        if (letter not in finKey):
            finKey += letter
    
    PFCMatrix = populate_matrix_with_key(finKey, create_n_matrix(5))
    
    PFCMatrix = poupulate_with_rest_of_alpha(finKey, PFCMatrix)
    
    
    
    return PFCMatrix




D = playfair("d", testKey, "D")



