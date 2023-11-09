import numpy as np
import sympy as sp
import metodos 

#Problema 1 letra A

# Defina a variável simbólica
x = sp.symbols('x')

# Defina a função simbólica
funcao = ((1500 * (1 + x)**240) - 1500) / 750000 - x
derivada = sp.diff(funcao,x)

[taxa, erro, n_iteracoes] = metodos.Newton(funcao, derivada, 1, 1e-6, 1000)

print(f"O valor estimado da raiz da função é {taxa} com um erro de {erro} em {n_iteracoes} iterações.")


#Problema 1 letra B

