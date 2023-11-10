import numpy as np
import sympy as sp

def bisection(f, a, b, tolerance, n_max):
    a = float(a)
    b = float(b)
    x = sp.Symbol('x')
    
    if f.subs(x, float(a)) * f.subs(x, float(b)) >= 0:
        print("As funções f.subs(x,a) e f.subs(x,b) deve ter sinais diferentes.")
        return

    c = a
    cont = 1
    
    while abs(f.subs(x,float(c))) > tolerance and cont <= n_max:
        c = (a + b) / 2
        if abs(f.subs(x,float(c))) < tolerance:
            break
        if f.subs(x,float(c)) * f.subs(x,float(a)) < 0:
            b = float(c)
        else:
            a = float(c)
        if cont==1:
            x0 = float(c)
        elif cont==2:
            x1 = float(c)
            
        cont+=1
        
    else:
        print("O maximo de iterações foi alcançado.")

    return c, abs(f.subs(x,float(c))), cont, x0, x1


def regulaFalsi(f, a, b, tolerance, n_max):
    a = float(a)
    b = float(b)
    x = sp.Symbol('x')


    if f.subs(x, a) * f.subs(x, b) >= 0:
        print("As funções f(a) e f(b) devem ter sinais diferentes.")
        return

    iteracoes = 1
    while iteracoes <= n_max:
        c = (a * f.subs(x, b) - b * f.subs(x, a)) / (f.subs(x, b) - f.subs(x, a))
        if abs(f.subs(x, c)) < tolerance:
            break
        elif f.subs(x, a) * f.subs(x,c) < 0:
            b = float(c)
        else:
            a = float(c)
        iteracoes += 1

    return c, abs(f.subs(x, float(c))), iteracoes

def FixedPoint(f, phi, a, b, tolerance, n_max):
    a = float(a)
    b = float(b)

    x=sp.Symbol('x')
    if f.subs(x,float(a)) * f.subs(x,float(b)) >= 0:
        print("As funções f.subs(x,a) e f.subs(x,b) deve ter sinais diferentes.")
        return

    # função para encontrar o ponto fixo
    def g(xi):
        return phi.subs(x,xi) - xi

    # itera até convergir
    n = 0
    c = float(b)
    iteracoes = 1
    while abs(g(float(c))) > tolerance and iteracoes <= n_max:
        n_max -= 1
        c = phi.subs(x,c)
        n += 1
        iteracoes+=1

    return c, abs(g(float(c))), iteracoes


def Newton(f, df, x0, tolerance, n_max):
    x0 = float(x0)
    x=sp.Symbol('x')
    
    # inicializa as variaveis de iteração
    n = 0
    c = float(x0)
    iteracoes = 1
    # itera até convergir
    while abs(f.subs(x,float(c))) > tolerance and iteracoes <= n_max:
        c = c - f.subs(x,float(c)) / df.subs(x,float(c))
        n += 1
        iteracoes+=1

    return c, abs(f.subs(x,float(c))), iteracoes


def Secant(f, x0, x1, tolerance, n_max):
    x0 = float(x0)
    x1 = float(x1)

    xSimbolico=sp.Symbol('x')
    print(x0,x1,f.subs(xSimbolico,float(x0)) , f.subs(xSimbolico,float(x1)))
    # Check if the initial guesses bracket a root
    # if f.subs(xSimbolico,float(x0)) * f.subs(xSimbolico,float(x1)) >= 0:
    #     print("As funções f.subs(x,a) e f.subs(x,b) deve ter sinais diferentes.")
    #     return

    # Itera usando metodo da secante
    for n in range(n_max):
        x = x1 - f.subs(xSimbolico,float(x1)) * (float(x1) - float(x0)) / (f.subs(xSimbolico,float(x1)) - f.subs(xSimbolico,float(x0)))
        print(x)
        # se a raiz foi encontrada, returna o resultado
        if abs(f.subs(xSimbolico,float(x))) <= tolerance:
            return x, abs(f.subs(xSimbolico,float(x))), n

        # se não, prepara para a proxima iteração
        x0, x1 = x1, x
        
    # Se o numero maximo de iterações foi alcançado, mostra o erro
    print("O maximo de iterações foi alcançado.")