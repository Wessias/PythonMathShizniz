# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 21:18:32 2022

@author: Jag
"""

#RUN THIS FIRST
import numpy as np
import numpy.linalg as ln
import scipy.optimize as opt 
import matplotlib.pyplot as plt

e = np.e


# %%
#GREVE RUMFORD

t = np.array([4,5,7,12,14,16,20,24,28,31,34,37.5,41])  #Tid
T = np.array([126,125,124,120,119,118,116,115,114,113,112,111,110]) #Temp (Fahrenheit)
T_env = 60 #Temp of environment
T_0 = 130 #Start temp
plt.figure(dpi=300)
plt.plot(t, T, "k.", label= "Data Points", color="purple")


#Way numero 1:
t1 = np.linspace(0,45)
    
#ln((T - T_env) / (T_0 - T_env)) = -Bt

def lstsqWay():
    
    b = np.log((T - T_env) / (T_0 - T_env))

    B = np.float64( -1 * ln.lstsq(np.asmatrix(t).T,  np.asmatrix(b).T, rcond=None)[0])



    plt.plot(t1, (T_env + (T_0 - T_env)*e**(-B*t1)), )
    return B

    
    
b1 = lstsqWay()


#Way numero 2:
    
def opt1():
    n = lambda B : (ln.norm(T - (T_env + (T_0 - T_env)*e**(-B*t))))**2
    B = opt.minimize(n,1).x
    plt.plot(t1, (T_env + (T_0 - T_env)*e**(-B*t1)) )
    return B
    
    
    
    
b2 = opt1()




#Way numero 3:
def func(vec):
    return (ln.norm(T - (vec[0] + (T_0 - vec[0])*e**(vec[1]*-t))))**2
    

def opt2():
    approx = opt.minimize(func, [100,0.5])
    
    return approx.x

b3 = opt2()
plt.plot(t1, (b3[0] + (T_0 - b3[0])*e**(b3[1]*-t1)))


plt.legend(["Data Point", "Least Square Method", "SciPy Minimize B", "SciPy Minimize B and T_omg"])



# %%

#ANPASSA POTENSFUNKTION y = ax^b

x = np.array([1.000e-03, 1.584e-02, 2.511e-01, 3.981e+00, 6.309e+01, 1.000e+03])
y = np.array([3.155e-04, 1.787e-02, 3.475e-01, 9.596e+00, 5.388e+02, 7.147e+03])
plt.figure(dpi=300)
x1 = np.linspace(0, 10**3.2)
y1 = np.linspace(0, 10**4)
plt.loglog(x, y, ".k", color="purple")


# ln(y) = ln(a) + b * ln(x)
def lstsqWay():
    A = np.transpose([[1,1,1,1,1,1], np.log(x) ])
    yVec = np.log(y)
    approx = ln.lstsq(A,yVec)
    a, b = e**(approx[0][0]), approx[0][1]
    r = (ln.norm(a*x**(b) - y))**2
    
    return a, b, r

a1, b1, r1 = lstsqWay()

plt.loglog(x1, a1*x1**(b1), color="black")

def func1(vec):
    return (ln.norm(vec[0]*x**(vec[1]) - y))**2

def opt1():
    approx = opt.minimize(func1, [0,0])
    
    return approx.x

a2, b2 = opt1()[0], opt1()[1]
r2 = (ln.norm(a2*x**(b2) - y))**2

plt.loglog(x1, a2*x1**(b2), color="pink")


def func2(vec):
    return ((ln.norm((vec[0]*x**(vec[1]))/(y) - 1)))**2

def opt2():
    approx = opt.minimize(func2, [1,1])
    return approx.x

a3, b3 = opt2()[0], opt2()[1]
r3 = (ln.norm(a3*x**(b3) - y))**2

plt.loglog(x1, a3*x1**(b3))

plt.legend(["Data Point", "Least Square Method", "SciPy Minimize ax^b", "SciPy Minimize (ax^b)/y"])


# %%

#NEWTONS METHOD
xs = np.array([ 1.23, 0.12, -0.22])
ys = np.array([ 0.01, 0.98, 0.02])
zs = np.array([-0.11, -0.12, 1.76])
r = np.array([1.22, 0.98, 1.52])

def f(p):
    
    f =  np.array([[(p[0] - xs[0])**2 + (p[1] - ys[0])**2 + (p[2] - zs[0])**2 - r[0]**2], 
         [(p[0] - xs[1])**2 + (p[1] - ys[1])**2 + (p[2] - zs[1])**2 - r[1]**2], 
         [(p[0] - xs[2])**2 + (p[1] - ys[2])**2 + (p[2] - zs[2])**2 - r[2]**2]])
    f.shape = (3,1)
    
    return f


def j(p):

    j = np.array([[2*(p[0] - xs[0]), 2*(p[1] - ys[0]), 2*(p[2] - zs[0])],
         [2*(p[0] - xs[1]), 2*(p[1] - ys[1]), 2*(p[2] - zs[1])], 
         [2*(p[0] - xs[2]), 2*(p[1] - ys[2]), 2*(p[2] - zs[2])]])
    j.shape = (3,3)
    
    return j

def newtonMeth(guess): 
    p = guess
    n = 0
    while(True):
        p1 = p - np.matmul(ln.inv(j(p)), f(p))
        
        if (ln.norm(p1 - p) < 10**(-5)): #Why not in the while statement? I don't know.
            return (p1, n)
        
        n += 1
        p = p1



g1 = newtonMeth(np.array([[0],[0],[0]]))
g2 = newtonMeth(np.array([[1],[1],[1]]))
g3 = newtonMeth(np.array([[0.3407007110432360],[0.3907070706849901],[0.4758069306448354]]))

print("Guess 1 gives sol",g1[0], "in", g1[1], "tries.")
print("Guess 2 gives sol",g2[0], "in", g2[1], "tries.")
print("Guess 3 gives sol",g3[0], "in", g3[1], "tries.")



