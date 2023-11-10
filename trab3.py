import numpy as np
import sympy as sp
import metodos
import matplotlib.pyplot as plt

#----------Configuração das fontes------------
fonte_titulo={  
              "fontsize":14,
              "fontweight": 'bold',
              #"fontname":'Times New Roman',
              }
fonte_labels={
            "fontsize":12,
            "fontweight":'bold',
            #'fontname':'Times New Roman',
            }
fonte_legenda={
            "size":9,
            "weight":'normal',
            #'family':'Times New Roman',
            }

# ---------------Funções---------------------------
def function1(x):
    return sp.exp(x) + 2**(-x) + 2 * sp.cos(x) - 6

def function2(x):
    return 2 * x * sp.cos(2 * x) - (x - 2)**2

def function3(x):
    return sp.exp(x) - 3*x**2

# ----------------Derivada--------------------------
def derivatefunction(funcao):
    x = sp.Symbol('x')
    return sp.diff(funcao, x)

# -----------------MAIN------------------------------

x = sp.Symbol('x')

funcoes = []
funcoes.append(function1(x))
funcoes.append(function2(x))
funcoes.append(function3(x))

derivadas = []
derivadas.append(derivatefunction(funcoes[0]))
derivadas.append(derivatefunction(funcoes[1]))
derivadas.append(derivatefunction(funcoes[2]))

# Vetores de Raízes
raizesBissecao = []
raizesFalsaPosicao = []
raizesPontoFixo = []
raizesNewton = []
raizesSecante = []

# Vetores para os erros
errosBissecao = []
errosFalsaPosicao = []
errosPontoFixo = []
errosNewton = []
errosSecante = []

# Vetores de iterações
iteracoesBissecao = []
iteracoesFalsaPosicao = []
iteracoesPontoFixo = []
iteracoesNewton = []
iteracoesSecante = []

# Funções PHI
phis = [sp.ln(6 - 2**(-x) - 2*sp.cos(x)), sp.acos(((x - 2)**2)/(2*x)), sp.ln(3*x**2), sp.ln(3*x**2)]

# Titulos para os gráficos
titulos = ["funcao_da_letra_a", "funcao_da_letra_b_x_2_3", "funcao_da_letra_b_x_3_4", "funcao_da_letra_c_x_0_1", "funcao_da_letra_c_x_3_5"]
# Controla qual função está sendo processada
contador = 0
# Tolerância para o erro
tolerancia = 0.00000001
# Número máximo de iterações
max_iter = 1000

for i in range(5):
    
    match contador:
        case 0:
            lb = 1; ub = 2
            phi = phis[0]
            funcao = funcoes[0]
            derivada = derivadas[0]
        case 1:
            lb = 2; ub = 3
            phi = phis[1]
            funcao = funcoes[1]
            derivada = derivadas[1]
        case 2:
            lb = 3; ub = 4
            phi = phis[1]
            funcao = funcoes[1]
            derivada = derivadas[1]
        case 3: 
            lb = 0; ub = 1
            phi = phis[2]
            funcao = funcoes[2]
            derivada = derivadas[2]
        case 4:
            lb = 3; ub = 5
            phi = phis[3] 
            funcao = funcoes[2]
            derivada = derivadas[2]
        case 5:
            lb = 3; ub = 5
            phi = phis[3] 
            funcao = funcoes[2]
            derivada = derivadas[2]
    print("----------------------------------------------------------------------------------")
    # Bisseção
    [raizBi, imagem_raizBi, n_iteracoesBi, x0, x1, errosBissecao, iteracoesBissecao] = metodos.bisection(funcao, lb, ub, tolerancia, max_iter)
    print("Terminei Bisseção")
    print(f"Erro: {imagem_raizBi}, Iteracoes: {iteracoesBissecao}")
    print()
    # Falsa Posição
    [raizFP, imagem_raizFP, n_iteracoesFP,errosFalsaPosicao,iteracoesFalsaPosicao] = metodos.regulaFalsi(funcao, lb, ub, tolerancia, max_iter)
    print("Terminei Falsa Posição")
    print(f"Erro: {imagem_raizFP}, Iteracoes: {iteracoesFalsaPosicao}")
    print()
    # Ponto Fixo
    [raizPF, imagem_raizPF, n_iteracoesPF] = metodos.FixedPoint(funcao, phi, lb, ub, tolerancia, max_iter)
    print("Terminei Ponto Fixo")
    print(f"Erro: {imagem_raizPF}, Iteracoes: {iteracoesFalsaPosicao}")
    print()
    # Newton
    [raizNew, imagem_raizNew, n_iteracoesNew] = metodos.Newton(funcao, derivada, x0, tolerancia, max_iter)
    print("Terminei Newton")
    print(f"Erro: {imagem_raizNew}, Iteracoes: {n_iteracoesNew}")
    print()
    # Secante
    [raizSec, imagem_raizSec, n_iteracoesSec] = metodos.Secant(funcao, x0, x1, tolerancia, max_iter)
    print("Terminei Secante")
    print(f"Erro: {imagem_raizSec}, Iteracoes: {n_iteracoesSec}")
    print()
    
    # Plots
    plt.title(titulos[contador], fontdict=fonte_titulo)
    plt.xlabel("Iterações", fontdict=fonte_labels)
    plt.ylabel("Erro Absoluto", fontdict=fonte_labels)
    plt.ylim(0,0.00000001)
    if contador == 4:
        plt.ylim(0,0.0000004)
    plt.grid(zorder = 1)
    #print(imagem_raizBi,iteracoesFalsaPosicao)
    plt.scatter(n_iteracoesBi, imagem_raizBi, marker='o', zorder = 2, label="Bisseção", s=50)
    plt.scatter(n_iteracoesFP, imagem_raizFP, marker='o', zorder = 2, label="Falsa Posição", s=50)
    plt.scatter(n_iteracoesPF, imagem_raizPF, marker='o', zorder = 2, label="Ponto Fixo", s=50)
    plt.scatter(n_iteracoesNew, imagem_raizNew, marker='o', zorder = 2, label="Newton", s=50)
    plt.scatter(n_iteracoesSec, imagem_raizSec, marker='o', zorder = 2, label="Secante", s=50)
    plt.legend(loc = "upper left", fancybox = False, prop = fonte_legenda)
    plt.savefig("./Graficos/Grafico"+titulos[contador]+".png")
    plt.close()
    
    contador+=1
     
print(contador)
# Print das derivadas
"""
for [funcao, derivada] in zip(funcoes, derivadas):
    print("Funcao: ")
    print(funcao)
    print("Derivada: ")
    print(derivada)
"""