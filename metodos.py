import numpy as np
import sympy as sp

def bisection(f, a, b, tolerance, n_max):
    
    x = sp.Symbol('x')
    
    if f.subs(x, a) * f.subs(x, b) >= 0:
        print("As funções f.subs(x,a) e f.subs(x,b) deve ter sinais diferentes.")
        return

    c = a
    cont = 1
    
    while abs(f.subs(x,c)) > tolerance and cont <= n_max:
        c = (a + b) / 2
        if abs(f.subs(x,c)) < tolerance:
            break
        if f.subs(x,c) * f.subs(x,a) < 0:
            b = c
        else:
            a = c
        if cont==1:
            x0 = c
        elif cont==2:
            x1 = c
            
        cont+=1
        
    else:
        print("O maximo de iterações foi alcançado.")

    return c, abs(f.subs(x,c)), cont, x0, x1


def regulaFalsi(f, a, b, tolerance, n_max):
    x = sp.Symbol('x')

    if f.subs(x, a) * f.subs(x, b) >= 0:
        print("As funções f(a) e f(b) devem ter sinais diferentes.")
        return

    iteracoes = 1
    while iteracoes <= n_max:
        c = (a * f.subs(x, b) - b * f.subs(x, a)) / (f.subs(x, b) - f.subs(x, a))
        if abs(f.subs(x, c)) < tolerance:
            break
        elif f.subs(x, a) * f.subs(x, c) < 0:
            b = c
        else:
            a = c
        iteracoes += 1

    return c, abs(f.subs(x, c)), iteracoes

def FixedPoint(f, phi, a, b, tolerance, n_max):
    
    x=sp.Symbol('x')
    
    if f.subs(x,a) * f.subs(x,b) >= 0:
        print("As funções f.subs(x,a) e f.subs(x,b) deve ter sinais diferentes.")
        return

    # function to find fixed point
    def g(x):
        return phi(x) - x

    # iterate until convergence
    n = 0
    c = b
    iteracoes = 1
    while abs(g(c)) > tolerance and iteracoes <= n_max:
        n_max -= 1
        c = phi(c)
        n += 1
        iteracoes+=1

    return c, abs(g(c)), iteracoes


def Newton(f, df, x0, tolerance, n_max):
    
    x=sp.Symbol('x')
    
    # initialize iteration variables
    n = 0
    c = x0
    iteracoes = 1
    # iterate until convergence
    while abs(f.subs(x,c)) > tolerance and iteracoes <= n_max:
        n_max -= 1
        c = c - f.subs(x,c) / df.subs(x,c)
        n += 1
        iteracoes+=1

    return c, abs(f.subs(x,c)), iteracoes


def Secant(f, x0, x1, tolerance, n_max):
    
    xSimbolico=sp.Symbol('x')
    
    # Check if the initial guesses bracket a root
    if f.subs(x,x0) * f.subs(x,x1) >= 0:
        print("As funções f.subs(x,a) e f.subs(x,b) deve ter sinais diferentes.")
        return

    # Iterate using the Secant method
    for n in range(n_max):
        x = x1 - f.subs(xSimbolico,x1) * (x1 - x0) / (f.subs(xSimbolico,x1) - f.subs(xSimbolico,x0))

        # If the root has been found, return the result
        if abs(f.subs(xSimbolico,x)) <= tolerance:
            return x, abs(f.subs(xSimbolico,x)), n

        # If not, prepare for the next iteration
        x0, x1 = x1, x
        
    # If the maximum number of iterations has been reached, raise an error
    print("O maximo de iterações foi alcançado.")