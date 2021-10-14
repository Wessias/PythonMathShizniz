# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:55:03 2021

@author: Regnd
"""

#1. Egna funktioner
#
#    Skriv en funktion korsar_x_axeln som har två inparametrar k och m. 
# Den ska returnera värdet på x där linjen y=kx+m korsar x-axeln om linjen korsar x-axeln. 
#Om linjen inte korsar x-axeln ska den istället returnera strängen "Inget svar". 
#Bland fallen att linjen inte korsar x-axeln finns det ett speciellt fall, vilket då? 
#    Skriv kod som låter användaren mata in k och m och sedan anropar funktionen korsar_x_axeln med dessa som inparametrar
# och sparar det returnerade värdet i en variabel svar.
#    Om linjen korsade x-axeln så skriv ut x-värdet där den korsar 
#med förklarande text, annars skriv ut texten Linjen korsar inte x-axeln.

import numpy as np
import matplotlib.pyplot as plt
from numpy import random

def findXThatCrossesXAxis(k, m):
    if(k == 0):
        return ("No answer")
    else:
        return (-m/k)
    

kIn = float(input("Choose a value for k in y = kx + m "))
mIn = float(input("Choose a value for m in y = kx + m "))

xValueOfCross = findXThatCrossesXAxis(kIn, mIn)

if(str(xValueOfCross) == "No answer"):
    print("Line does not cross the x axis")  
else:
    print("The line y = " + str(kIn) + "x +", mIn , "crosses the x axis at the x value of", xValueOfCross)
    
    
    
    
   # Skapar en variabel arr av typen ndarray som innehåller 
   #alla positiva heltal från ett till en miljon. (Tips: använd np.arange.)
#Beräknar genom att använda en universell funktion i NumPy följande summa ∑106i=1sin(i)
#. (Tips: använd np.sin och np.sum) Max två rader kod!
#Beräknar summan ∑106i=11i
#. Återigen max två rader kod.
    


arr = np.arange(1,1000001)
arr = np.int64(arr)
Simdim = np.sum(arr)
SumArr = np.sin(arr)
Sum1 = np.sum(SumArr)
temparr = arr.astype(float)
arr2 = np.reciprocal(temparr)
Sum2 = np.sum(arr2)





xValues = np.linspace(0,2, 100)
f0 = np.sqrt(xValues)
f1 = xValues
f2 = np.power(xValues, 2)
f3 = np.power(xValues, 3)

#Rita alla i samma fönster men med olika färg och en ska vara streckad, en punktlinje, en heldragen 
#och en med omväxlande linje och punkt. Skapa också en nyckel som anger vilka funktionerna är.

plt.figure(1)
plt.plot(xValues, f0, "g", label="f(x)=sqrt(x)")
plt.plot(xValues, f1, 'k--', label="g(x)=x")
plt.plot(xValues, f2, 'c-o', label="h(x)=x^2", markersize=4)
plt.plot(xValues, f3, 'ro', label="i(x)=x^3", markersize=3)

plt.legend()

plt.figure(2)

x = random.rand(500) # Skapa ett fält med 500 slumpflyttal n med 0 < n < 1 
y = random.rand(500) # Skapa ett fält med 500 slumpflyttal n med 0 < n < 1 
farg = np.arctan(x/y) # Skapar lista med vinkeln mellan x-axeln och linjen till respektive punkt
storlek = 50 * np.sqrt(x**2 + y**2) # Skapar lista med avstånden till origo
plt.scatter(x, y, c = farg, s = storlek, alpha = 0.5) # Plotta cirklar med färg baserat på vinkel 
                                                   # och storlek baserat på avstånd från origo
                                                   # alpha = 0.5 gör dem transparenta
samma = 0
sinna = 0
recisum = 0
for i in range(1, 1000001):
    samma += i
    sinna += np.sin(i)
    recisum += (1 / i)
    pass
print(str(samma))











