import numpy as numpaj
from sympy import *
import matplotlib.pyplot as proto
import math
x = Symbol("x")

def min_NewtonRaphson(f, Df, x0, tol):
    f = lambdify(x, f)
    Df = lambdify(x, Df)
    print("START POINT IS", x0)
    
    while(numpaj.round(f(x0), tol) != 0):
        x0 = x0 - (f(x0) / Df(x0))
        print("Current x is", x0, "with the function value", f(x0))
    return numpaj.round(x0, tol)


y = 0.25*(x-4)**2 - 4*cos(5*x)-1.2
yPrim = y.diff(x)

m = min_NewtonRaphson(y, yPrim, -0.25, 4)
print(m)

x1 = numpaj.linspace(-1,1)
y = lambdify(x, y)

proto.plot(x1, y(x1))
proto.grid()
proto.axhline(y=0)