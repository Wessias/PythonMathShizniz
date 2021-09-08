# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:17:34 2021

@author: Regnd
"""

import math
import cmath

pi = math.pi

v1 = 0
v2 = pi/6
v3 = 2*pi/(6)
v4 = pi/2

listOfAngles = {v1, v2, v3, v4}



for angle in listOfAngles:
    angleAsStr = str(angle)
    print("sin of " + angleAsStr + " = " + str(math.sin(angle)))
    print("cos of " + angleAsStr + " = " + str(math.cos(angle)))
    print("tan of " + angleAsStr + " = " + str(math.tan(angle)))
    


# x^2 + ax+ b = 0

# x^2 + ax + b + a^2/4 - a^2/4 = 0
# (x + a/2)^2 + b - a^2/4 = 0
# (x + a/2)^2 + (4b-a^2)/4 = 0
# (x + a/2)^2 = (a^2-4b)/4
# x + a/2 = +-sqrt((a^2-4b)/4)
# x = -a/2 +- sqrt((a^2-4b)/4)

def SolutionsToSecondDegreeEquation(a, b):
    sol1 = ((-a/2) + (cmath.sqrt((math.pow(a,2)-4*b)/4)))
    sol2 = ((-a/2) - (cmath.sqrt((math.pow(a,2)-4*b)/4)))
    print("Solutions to equation are " + str(sol1) + " and " + str(sol2))
    
    
SolutionsToSecondDegreeEquation(5, 6)

c1 = float(input("The length of the first cathetus"))
c2 = float(input("The length of the second cathetus"))


def FindHypothenusAndAngles(cath1,cath2):
    hypo = math.sqrt((math.pow(cath1, 2) + math.pow(cath2, 2)))
    
    u = round(math.degrees((math.asin(cath1/hypo))), 2)
    v = round(math.degrees((math.asin(cath2/hypo))), 2)
    
    
    
    print( "Om kateterna är" , cath1 , "och" , str(cath2) , "så är hypotenusan" , hypo ,
          "och de spetsiga vinklarna", u , "och" , v)
    

FindHypothenusAndAngles(c1, c2)











    
    