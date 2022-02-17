# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 14:39:01 2022

@author: Regnd
"""

import numpy as np
import matplotlib.pyplot as plt



ax = plt.axes(projection="3d")

r = 1
t = np.linspace(0,2*np.pi)

h0 = 0
h2 = 2
x = r*np.cos(t)
y = r * np.sin(t)


ax.plot(x,y,h0)
ax.plot(x,y, h2)



a = np.pi/5
A = np.array([[np.cos(a), -np.sin(a),0],
[np.sin(a), np.cos(a), 0], [0,0,1]])


sPoint = np.linspace(0, 2 * np.pi, 21)

for t0 in sPoint:
    x0 = r * np.cos(t0)
    y0 = r * np.sin(t0)
    
    roofP = np.matmul(A, np.array([x0,y0,h2]) )
    
    
    ax.plot([x0,roofP[0]],[y0,roofP[1]],[0,roofP[2]])
    
    
ax.plot