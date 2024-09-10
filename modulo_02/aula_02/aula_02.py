import numpy as np

#Exercicios:
#1. De acordo com o array X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4]) faça a soma
#2. Faça a média

x1 = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
soma = np.sum(x1)
print(f'Soma do array: {soma}')

media = np.mean(x1)
print(f'Média do array: {media}')

#3. Dada a matriz faça a soma das colunas X = np.array([
#    [1,   2,  3,  4],
#    [5,   6,  7,  8],
#    [9,  10, 11, 12],
#    [13, 14, 15, 16]
#])
#4. Faça a média das linhas

x3 = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
somaColunas = np.sum(x3,axis=0)
print(f'A soma das colunas é: {somaColunas}')

mediaLinhas = np.mean(x3,axis=1)
print(f'A média das linhas é: {mediaLinhas}')

#5. Dado o array X = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10]) Mostre o elemento de maior valor

x5 = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])
x5.max()