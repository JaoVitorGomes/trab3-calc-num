import numpy as np
import sympy as sp
import metodos
import matplotlib.pyplot as plt

#----------Configuração das fontes------------
fonte_titulo={  
              "fontsize":14,
              "fontweight": 'bold',
              "fontname":'Times New Roman',
              }
fonte_labels={
            "fontsize":12,
            "fontweight":'bold',
            'fontname':'Times New Roman',
            }
fonte_legenda={
            "size":9,
            "weight":'normal',
            'family':'Times New Roman',
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

# Titulos para os gráficos
titulos = ["Gráfico função da letra a)", "Gráfico função da letra b) x -> [2,3]", "Gráfico função da letra b) x -> [3,4]", "Gráfico função da letra c) x -> [0,1]", "Gráfico função da letra c) x -> [3,5]"]
# Controla qual função está sendo processada
contador = 0
# Tolerância para o erro
tolerancia = 0.00000001
# Número máximo de iterações
max_iter = 1000

for [funcao, derivada] in zip(funcoes, derivadas):
    match contador:
        case 0:
            lb = 1; ub = 2
        case 1:
            lb = 2; ub = 3
        case 2:
            lb = 3; ub = 4
        case 3: 
            lb = 0; ub = 1
        case 4:
            lb = 3; ub = 5 
    
    # Bisseção
    [raizBi, imagem_raizBi, n_iteracoesBi, x0, x1] = metodos.bisection(funcao, lb, ub, tolerancia, max_iter)
    print("Terminei Bisseção")
    # Falsa Posição
    [raizFP, imagem_raizFP, n_iteracoesFP] = metodos.regulaFalsi(funcao, lb, ub, tolerancia, max_iter)
    print("Terminei Falsa Posição")
    # Ponto Fixo
    [raizPF, imagem_raizPF, n_iteracoesPF] = metodos.FixedPoint(funcao, funcao/derivada,lb, ub, tolerancia, max_iter)
    print("Terminei Ponto Fixo")
    # Newton
    [raizNew, imagem_raizNew, n_iteracoesNew] = metodos.Newton(funcao,derivada,x0, tolerancia, max_iter)
    print("Terminei Newton")
    # Secante
    [raizSec, imagem_raizSec, n_iteracoesSec] = metodos.Secant(funcao, x0, x1, tolerancia, max_iter)
    print("Terminei Secante")
    
    
    # Plots
    plt.title(titulos[contador], fontdict=fonte_titulo)
    plt.xlabel("Iterções", fontdict=fonte_labels)
    plt.ylabel("Erro Absoluto", fontdict=fonte_labels)
    plt.ylim(0,1)
    plt.grid(zorder = 1)
    plt.scatter(imagem_raizBi, errosBissecao, marker='o', zorder = 2, label="Bisseção", s=100)
    plt.scatter(imagem_raizFP, errosFalsaPosicao, marker='o', zorder = 2, label="Falsa Posição", s=100)
    plt.scatter(imagem_raizPF, errosPontoFixo, marker='o', zorder = 2, label="Ponto Fixo", s=100)
    plt.scatter(imagem_raizNew, errosNewton, marker='o', zorder = 2, label="Newton", s=100)
    plt.scatter(imagem_raizSec, errosSecante, marker='o', zorder = 2, label="Secante", s=100)
    plt.legend(loc = "upper left", fancybox = False, prop = fonte_legenda)
    plt.savefig("./Graficos/Grafico"+titulos[contador]+".png")
    
    contador+=1
    

# Print das derivadas
"""
for [funcao, derivada] in zip(funcoes, derivadas):
    print("Funcao: ")
    print(funcao)
    print("Derivada: ")
    print(derivada)
"""