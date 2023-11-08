import numpy as np
from sympy import diff, Symbol


def function(x):
    return x**3 - 9*x**2 + 24*x - 24

def derivatefunction(x):
    return 3*x**2 - 18*x + 24

def bisection(f, a, b, tolerance, n_max):
    if f(a) * f(b) >= 0:
        print("As funções f(a) e f(b) deve ter sinais diferentes.")
        return

    c = a
    for i in range(n_max):
        c = (a + b) / 2
        if abs(f(c)) < tolerance:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    else:
        print("O maximo de iterações foi alcançado.")

    return c, abs(f(c)), i


def regulaFalsi(f, a, b, tolerance, n_max):
    
    if f(a) * f(b) >= 0:
        print("As funções f(a) e f(b) deve ter sinais diferentes.")
        return
    
    c = b
    while abs(f(c)) > tolerance and n_max > 0:
        n_max -= 1
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c, abs(f(c)), n_max


def FixedPoint(f, phi, a, b, tolerance, n_max):
    if f(a) * f(b) >= 0:
        print("As funções f(a) e f(b) deve ter sinais diferentes.")
        return

    # function to find fixed point
    def g(x):
        return phi(x) - x

    # iterate until convergence
    n = 0
    c = b
    while abs(g(c)) > tolerance and n_max > 0:
        n_max -= 1
        c = phi(c)
        n += 1

    return c, abs(g(c)), n_max


def Newton(f, df, x0, tolerance, n_max):
    # initialize iteration variables
    n = 0
    c = x0

    # iterate until convergence
    while abs(f(c)) > tolerance and n_max > 0:
        n_max -= 1
        c = c - f(c) / df(c)
        n += 1

    return c, abs(f(c)), n_max


def Secant(f, x0, x1, tolerance, n_max):
    # Check if the initial guesses bracket a root
    if f(x0) * f(x1) >= 0:
        print("As funções f(a) e f(b) deve ter sinais diferentes.")
        return

    # Iterate using the Secant method
    for n in range(n_max):
        x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        # If the root has been found, return the result
        if abs(f(x)) < tolerance:
            return x, abs(f(x)), n

        # If not, prepare for the next iteration
        x0, x1 = x1, x

    # If the maximum number of iterations has been reached, raise an error
    print("O maximo de iterações foi alcançado.")


phi = lambda x: function(x) / derivatefunction(x)
listas_funcoes = ['bisection','regulaFalsi']

x = Symbol('x')
#print("valor do diff",diff(function,x))


for nome_funcao in listas_funcoes:
    x, error, n = globals()[nome_funcao](function, 0, 6, 1e-6, 100)
    print(f"O valor estimado da raiz da função é {x} com um erro de {error} em {n} iterações.")

x, error, n = FixedPoint(function, phi,0, 6, 1e-6, 100)
print(f"O valor estimado da raiz da função é {x} com um erro de {error} em {n} iterações.")

x,error,n = Newton(function, derivatefunction, 1,1e-6,100)
print(f"O valor estimado da raiz da função é {x} com um erro de {error} em {n} iterações.")

x,error,n = Secant(function, 0, 6,1e-6,100)
print(f"O valor estimado da raiz da função é {x} com um erro de {error} em {n} iterações.")

