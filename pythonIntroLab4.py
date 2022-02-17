# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 13:49:10 2022

@author: Regnd
"""
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image



#760 x 580 images







imgLocation = ""

curDir = ""
picDir = os.walk("./pictures/labb4") #walk returns list (generator) of 3 tuples (dirpath, dirnames, filenames)






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



# 1. totala antalet bildfiler
# 2. minsta antalet plus i en fil och namnen på de filer som har detta minsta antal
# 3. största antalet plus i en fil och namnen på de filer som har detta största antal
# 4. medelvärdet av antalet plus
# 5. totala antalet plus




fileCount = 0
searchedFiles = []
minGplus = [10000,[]] #[Amount, [files]]
maxGplus = [0,[]]
averageGplus = 0
totalGplus = 0
histData = []

for dirpath, dirname, files in picDir:
    for file in files:
        if (len(file) > 4 and file[-4:] == ".bmp"):
            
            imStr = dirpath + "/" + file
            tempIm = Image.open(dirpath + "/" + file)
            tempMatrix = np.asarray(tempIm)
            tempGplus = find_gPlus_in_imageMatrix(tempMatrix)
            
            totalGplus += tempGplus
            histData.append(tempGplus)
            fileCount += 1
            searchedFiles.append(file)
            
            if (tempGplus >= maxGplus[0]):
                if (maxGplus[0] == tempGplus):
                    maxGplus[1].append(file)
                else:
                    maxGplus[0] = tempGplus
                    maxGplus[1].clear()
                    maxGplus[1].append(file)
                
            if (tempGplus <= minGplus[0]):
                if(minGplus[0] == tempGplus):
                    minGplus[1].append(file)
                else:
                    minGplus[0] = tempGplus
                    minGplus[1].clear()
                    minGplus[1].append(file)
                    


averageGplus = totalGplus / fileCount
plt.hist(histData, color="purple", bins=30)
plt.title("Histogram of green pluses in pictures")
plt.grid(True)
plt.xlabel("Green Pluses")
plt.ylabel("Pictures")


print("PICTURES SEARCHED:", fileCount, 
      "\nTOTAL GREEN PLUSES:",totalGplus,
      "\nMAX GREEN PLUSES AND ACCOMPANYING PICTURES WITH THIS MAX:", maxGplus, 
      "\nMIN GREEN PLUSES AND ACCOMPANYING PICTURES WITH THE MIN:",minGplus, 
      "\nAVERAGE GREEN PLUSES IN A PICTURE:", averageGplus)
                
                
            
    
    















