import sympy as sp
import numpy as np

x = sp.Symbol('x')

#--------------FUNÇÃO A)-----------------
funcao = sp.ln(6 - 2**(-x) - 2*sp.cos(x))
derivada = sp.diff(funcao, x)

valores = np.arange(1, 2, 0.001)

passou = False

for valor in valores:
    #print(derivada.subs(x, valor))
    if derivada.subs(x, valor) >= 1:
        passou = True
        
print(passou)

#--------------FUNÇÃO B)-----------------
funcao = sp.acos(((x - 2)**2)/(2*x))
derivada = sp.diff(funcao, x)

valores = np.arange(2, 3, 0.001)

passou = False

for valor in valores:
    #print(derivada.subs(x, valor))
    if derivada.subs(x, valor) >= 1:
        passou = True
        
print(passou)

valores = np.arange(3, 4, 0.001)

passou = False

for valor in valores:
    #print(derivada.subs(x, valor))
    if derivada.subs(x, valor) >= 1:
        passou = True
        
print(passou)

#--------------FUNÇÃO C)-----------------
funcao = sp.sqrt(sp.exp(x)/3)
derivada = sp.diff(funcao, x)

valores = np.arange(0,1,0.001)

passou = False

for valor in valores:
    #print(derivada.subs(x, valor))
    if derivada.subs(x, valor) >= 1:
        passou = True
        
print(passou)

# A função abaixo daria problema para o intervalo [0,1], mas aqui sua derivada < 1 para todo valor do intervalo, 
# Ao passo que a função acima, sp.sqrt(sp.exp(x)/3), nesse intervalo daqui fica > 1, logo, não serve para esse intervalo
funcao = sp.ln(3*x**2)
derivada = sp.diff(funcao, x)
valores = np.arange(3,5,0.001)

passou = False

for valor in valores:
    #print(derivada.subs(x, valor))
    if derivada.subs(x, valor) >= 1:
        passou = True
        
print(passou)





