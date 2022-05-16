# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:30:48 2022

@author: Regnd
"""

import numpy as np #Basic linear algebra
import numpy.linalg as ln #Matrix solvers/eigenvalues
import scipy.optimize as opt #Optimization library
import matplotlib.pyplot as plt #Plotting
import scipy.integrate as isc #Integration tools
import sympy as sym #Symbolic algebra
import scipy.interpolate as ap # Approximation tools
#%%
#Integrals

f = lambda x : x**(-9/10)*np.cos(x)

print(isc.quad(f, 0, 1)[0])
#print(isc.quadrature(f, 0, 1)[0])

f1 = lambda x : 10*x**(1/10)*np.sin(x)
f2 = lambda x : 10*x**(1/10)*np.cos(x)

#print(f2(1) - f2(0) + isc.quad(f1,0,1)[0])
#print(f2(1) - f2(0) + isc.quadrature(f1,0,1)[0])

p = 1729

f3 = lambda y : p*y**( (p/10) - 1 )*np.cos(y**p)


print(isc.quad(f3, 0, 1)[0])
print(isc.quadrature(f3, 0, 1)[0])




#%%
#Integrate x^k * sin(sqrt(3x)) from 0 to 1

x = sym.symbols("x")
k = 2

expr = x**(k) * sym.sin(sym.sqrt(3)*x)

I = sym.integrate(expr, (x, 0, 1))
print(I.evalf())


#%%
#Integrate Table

R = 0.5
N = 3
r = R/N
c = (R+r)/r

v = sym.symbols("v")
q = sym.symbols("q")

x = c*r*sym.cos(v)-q*r*sym.cos(c*v)
y = c*r*sym.sin(v) - q*r*sym.sin(c*v)

expr = sym.sqrt( (sym.diff(x, v))**2 + (sym.diff(y, v))**2 )


def O(q):
    
    #dx c*r*(q*np.sin(c*v) - np.sin(v))
    #dy  c*r*(np.cos(v) - q*np.cos(c*v))
    f = lambda v : np.sqrt(  (c*r*(q*np.sin(c*v) - np.sin(v)))**2 + 
                           (c*r*(np.cos(v) - q*np.cos(c*v)))**2  )
    I = isc.quad(f, 0, 2*np.pi)[0]
    
    return I


def func(q):
    return O(q) - 4.25

qSol = opt.fsolve(func, 1)
print(qSol[0])

#%%
#Interpolation

t = np.linspace(-2,3,8)
t1 = np.linspace(-2,3)
y1 = np.exp(-t**2)
y2 = np.array([-1,-1,-1,-1,1,1,1,1])


A = ap.interp1d(t, y1, kind="linear")
B = ap.interp1d(t, y1, kind="cubic")
C = ap.PchipInterpolator(t, y1)

plt.figure(dpi=300)

plt.figure(1)
plt.ylabel("y", loc="top")
plt.xlabel("t", loc="right")
plt.plot(t,y1, "o", color="black")
plt.plot(t1, A(t1), color="orange")
plt.plot(t1, B(t1), "--", color="Green" )
plt.plot(t1, C(t1), dashes=[2,2,10,2], color = "red")
plt.plot(t1, np.e**(-t1**2), )
plt.legend(["Data Punkter", "Linjär Interpolation", "Spline Interpolation", "Form Bevarande Interpolation", "Exakta Funktion"],
           fontsize="x-small")


D = ap.interp1d(t, y2, kind="linear")
E = ap.interp1d(t, y2, kind="cubic")
F = ap.PchipInterpolator(t, y2)

plt.figure(2)
plt.figure(dpi=300)
plt.ylabel("y", loc="top")
plt.xlabel("t", loc="right")
plt.plot(t,y2, "o", color="black")
plt.plot(t1, D(t1), color="orange")
plt.plot(t1, E(t1), "--", color="Green" )
plt.plot(t1, F(t1), dashes=[2,2,10,2], color = "red")
plt.legend(["Data Punkter", "Linjär Interpolation", "Spline Interpolation", "Form Bevarande Interpolation"],
           fontsize="x-small")





#%%
#Fields and gifs

# List of point charges
points = [np.array([-1,-0.9]),
np.array([1,-0.9])]

c = 10**(-5)
def dydt(t,y):
    # Assignment: change this this to the y’(t) you derived
    yp = np.array([0,0,0,0])
    
    return yp


# initial position (0.5,-0.9), no movement (0,0)
y0 = np.array([0.5,-0.9,0,0])


#integrate until t = 1000
t_end = 10**3


# Solve the initial value problem
result = isc.solve_ivp(dydt, (0,t_end), y0)


# This will create a 3+0.5s gif at 30fps.
from Lab3Animation import animate
animate(points, result, filename = "out.gif", aniSeconds=3,fps = 30)





