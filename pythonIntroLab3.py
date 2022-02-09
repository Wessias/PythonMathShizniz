# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 15:46:45 2022

@author: Regnd
"""




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
            tempList.append("")
            
        M.append(tempList)
    return M

#-----------------------------------------------------------------------------

def poupulate_with_rest_of_alpha(key, Matrix):
    alpha = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
    for letter in key:
        alpha = alpha.replace(letter, "")

    
    lettersAdded = 0
    for row in Matrix:
        for col in range(5):
            if (row[col] == ""):
                row[col] = alpha[lettersAdded]
                lettersAdded = lettersAdded + 1
    
    
    return Matrix

#-----------------------------------------------------------------------------


def list_of_split_string_in_pairs(text):
    tempText = ""
    
    for i in range(len(text) - 1): # -1 there to not fall out of index
        if (text[i] == text[i + 1] and (i % 2 == 0 or len(tempText) % 2 == 0)):
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


#-----------------------------------------------------------------------------


def find_item_index_in_square_matrix(matrix, item):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if (matrix[row][col] == item):
                return (row, col)



#-----------------------------------------------------------------------------


def cryptAlgo(letterPairs, matrix, crypt):
    
    cryptPairs = []
    
    
    move = -1 #Move left/up (In the matrix)
    if(crypt):
        move = 1 #Move right/down
        

    for pair in letterPairs:

        
        indexLetter1 = find_item_index_in_square_matrix(matrix, pair[0])
        indexLetter2 = find_item_index_in_square_matrix(matrix,pair[1])
        
        if(indexLetter1[0] == indexLetter2[0]):#Check if same row
            cryptPairs.append( matrix[indexLetter1[0]][(indexLetter1[1] + move) % 5] +
                              matrix[indexLetter2[0]][(indexLetter2[1] + move ) % 5] )
            
        elif(indexLetter1[1] == indexLetter2[1]):#Check if same col
            cryptPairs.append( matrix[(indexLetter1[0] + move) % 5][indexLetter1[1]] +
                               matrix[(indexLetter2[0] + move) % 5][indexLetter2[1]])
        
                
        else:
            #The letters stay in the same row but swap columns with each other
            tempPair = matrix[indexLetter1[0]][indexLetter2[1]] + matrix[indexLetter2[0]][indexLetter1[1]]
            cryptPairs.append(tempPair)
            
    
    print(cryptPairs)
    return cryptPairs


#-----------------------------------------------------------------------------

def playfair(text, key, crypt):
        
    finKey = ""
    for letter in key:
        if (letter not in finKey):
            finKey += letter
    
    
    PFCMatrix = populate_matrix_with_key(finKey, create_n_matrix(5))
    PFCMatrix = poupulate_with_rest_of_alpha(finKey, PFCMatrix)
    
 

    letterPairs = list_of_split_string_in_pairs(text)
    print(letterPairs)
    
    finalCrypt = cryptAlgo(letterPairs, PFCMatrix, crypt)
    
    strFinCrypt = ""
    for p in finalCrypt:
        strFinCrypt += p
        
    
    return strFinCrypt, PFCMatrix, finalCrypt



testKey = "PLAYFAIREXAMPLE"
testText = "HIDETHEGOLDINTHETREESTUMP"

chiffer = 'FLAPJBCZFAEMAUHJNREPGPDVUNLINGNWSRMCABAHTNOREPFESGFSEMBSAHGOHJNREPGPDVUNCRAJLAEMHJNGSRPAAMNEXUULHDLEDZ'
chifKey = "NOPRESSURENODIAMONDS"

D =  playfair(chiffer, chifKey, False)

E = playfair(D[0], chifKey, True)

