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
print("Anos necessarios para ganhar o dinheiro necessario = "+str(meses_necessarios/12))
print()


#--------------Problema 2 letra A--------------------
funcao = (0.90609*x*sp.exp(-x/3) - 1)
derivada = sp.diff(funcao,x)

[tempo, erro, n_iteracoes] = metodos.Newton(funcao, derivada, 0.75, 1e-5, 1000)
print(f"O Tempo estimado para atingir a concentração desejada {tempo} com um erro de {erro} em {n_iteracoes} iterações.")
print()

#--------------Problema 2 letra B--------------------
x = sp.symbols('x')
funcao = (0.90609 * x * sp.exp(-x/3) - 1)

# Calculando a derivada da função
derivada = sp.diff(funcao, x)

# Encontrando o tempo para atingir a concentração desejada inicial
[tempo_atingir_maximo, erro, n_iteracoes] = metodos.Newton(funcao, derivada, 0.75, 1e-5, 1000)
print(f"O Tempo estimado para atingir a concentração desejada é {tempo_atingir_maximo} horas com um erro de {erro} em {n_iteracoes} iterações.")
print()

# Encontrando o tempo para atingir a concentração de 0.25 mg/ml
[tempo_atingir_025, erro, n_iteracoes] = metodos.Newton(funcao, derivada, 1, 1e-5, 1000)
print(f"O Tempo estimado para atingir a concentração de 0.25 mg/ml é {tempo_atingir_025} horas com um erro de {erro} em {n_iteracoes} iterações.")
print()

# Agora, vamos calcular o tempo para a segunda injeção após a concentração cair para 0.25 mg/ml
# O novo ponto inicial para o método de Newton será o tempo_atingir_025
[tempo_segunda_injecao, erro, n_iteracoes] = metodos.Newton(funcao, derivada, tempo_atingir_025, 1e-5, 1000)
print(f"O Tempo estimado para a segunda injeção é {tempo_segunda_injecao} horas com um erro de {erro} em {n_iteracoes} iterações.")
print()