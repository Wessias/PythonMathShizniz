# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:07:06 2021

@author: Biggo
"""

import math
import random

list = []
antal = int(input("Number of elements in list"))

for i in range(0, antal):
    list.append(random.randint(1, 100))
    pass



S = 0

for number in list:
    S = S + number
    pass

print(S)
print(S/antal)

gräns = int(input("Välj en gräns"))
sumOfLn = 0
i = 1;


while(sumOfLn < gräns):
    sumOfLn = sumOfLn + math.log(i, math.e)
    i += 1
    
print("n är", i - 1)


#skapar två mängder A och B med 20 slumpmässigt valda heltal  n som uppfyller 1≤n≤100

A = set({})
B = set({})

while(True):
    if(len(A) != 20):
        A.add(random.randint(1, 100))
    
    if(len(B) != 20):
        B.add(random.randint(1, 100))
  
    if(len(A) == 20 and len(B) == 20):
        break;
    pass

#skriver ut antalet element i unionen respektive snittet mellan A och B
print(A.union(B)) 
print(A.intersection(B))



































