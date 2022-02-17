# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 14:58:52 2022

@author: Regnd
"""

import numpy as np
import matplotlib.pyplot as plt


ax = plt.axes(projection='3d')
plt.xlabel("X")
plt.ylabel("Y")




def do_circle(r, h):
    t = np.linspace(0, 2 * np.pi)
    x = r * np.cos(t)
    y = r * np.sin(t) 
    
    ax.plot(x,y,h, 'b')
    
    return

h = 1
for r in range(1,7):
    do_circle(r, h)
    do_circle(r, -h)
    h += 1
    