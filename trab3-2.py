import numpy as np
import sympy as sp
import metodos 


#--------------Problema 1 letra A------------------

x = sp.symbols('x')

# Defina a função simbólica
funcao = ((1500 * (1 + x)**240) - 1500) / 750000 - x
derivada = sp.diff(funcao,x)

[taxa, erro, n_iteracoes] = metodos.Newton(funcao, derivada, 0.05, 1e-6, 1000)
print()
print(f"O valor estimado da raiz da função é {taxa} com um erro de {erro} em {n_iteracoes} iterações.")
print()

#--------------Problema 1 letra B-------------------

funcao = ((1500 * (1 + ((sp.sin(x/2) + 1)**(10 * 10**(-4))))**240) - 1500) / 750000 - ((sp.sin(x/2) + 1)**(10 * 10**(-4)))
derivada = sp.diff(funcao, x)

[meses_necessarios, erro, n_iteracoes] = metodos.Newton(funcao, derivada, 10, 1e-6, 1000)
print("Meses necessarios para ganhar o dinheiro necessario = "+str(meses_necessarios/12))
print()


#--------------Problema 2 letra A--------------------
funcao = (0.9*x*sp.exp(-x/3) - 1)
derivada = sp.diff(funcao,x)

[tempo, erro, n_iteracoes] = metodos.Newton(funcao, derivada, 0.75, 1e-2, 1000)
print(f"O Tempo estimado para atingir a concentração desejada {tempo} com um erro de {erro} em {n_iteracoes} iterações.")
print()

#--------------Problema 2 letra B--------------------
funcao = (0.9*x*sp.exp(-x/3) - 1)
derivada = sp.diff(funcao,x)

[tempo, erro, n_iteracoes] = metodos.Newton(funcao, derivada, 0.75, 1e-2, 1000)
print(f"O Tempo estimado para atingir a concentração desejada {tempo} com um erro de {erro} em {n_iteracoes} iterações.")
print()
