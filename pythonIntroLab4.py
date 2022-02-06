# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 13:49:10 2022

@author: Regnd
"""
import numpy as np
import os
from PIL import Image



#760 x 580 images


print(os.listdir("./pictures/labb4/testpics/"))

im = Image.open("./pictures/labb4/testpics/testbild.bmp") #TESTPIC

imMat = np.asarray(im)

imgLocation = ""

curDir = "/"
q = list(os.walk("./pictures/labb4")) #walk returns list (generator) of 3 tuples (dirpath, dirnames, filenames)






#This function iterates through the matrix and finds green pluses. Green = 128
def find_gPlus_in_imageMatrix(matrix):
    gPlusCount = 0 #GREEN PLUS COUNTER
    rowMax = len(matrix) - 1
    colMax = len(matrix[0]) - 1
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])): #Hopefully most images are rectangular
            if(matrix[row][col] == 128): #Check if green pixel
                for i in range(1,3):
                    #Longest if statement to check that the indexs are in the bounds and the pixels are green
                    if(    col + i <= colMax #IF1
                       and col - i >= 0
                       and row + i <= rowMax 
                       and row - i >= 0 ):
                        
                        if (    matrix[row][col + i] == 128 
                            and matrix[row][col - i] == 128
                            and matrix[row + i][col] == 128
                            and matrix[row - i][col] == 128): #IF2
                            
                            if ( i == 2): #IF3
                                #If it gets this far its checked the 2 pixels up/down/left/right and if they're green
                                gPlusCount += 1
                            else: #IF3
                                continue
                    
                        else: #IF2
                            break
                    
                    else: #IF1
                        break
                        
            
            
        
    return gPlusCount


p = find_gPlus_in_imageMatrix(imMat)
