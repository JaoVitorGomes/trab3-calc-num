import numpy as np
from sympy import diff, symbols


#Problema 1 letra A
def function(x):
    return (1500/x)*((1 + x)**(20*12)  - 1) - 750000

def Newton(f, df, x0, tolerance, n_max):
    # initialize iteration variables
    n = 0
    c = x0

    # iterate until convergence
    while abs(f(c)) > tolerance and n < n_max:
        c = c - f(c) / df.subs('x', c)
        n += 1

    error = abs(f(c))
    return c, error, n

x = symbols('x')
dfun = diff(function(x), x)

root, error, n = Newton(function, dfun, 1, 1e-6, 100)
print(f"O valor estimado da raiz da função é {root} com um erro de {error} em {n} iterações.")


#Problema 1 letra B

