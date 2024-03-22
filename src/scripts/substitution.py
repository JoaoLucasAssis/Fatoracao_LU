import numpy as np

def forward_substitution(L, b):
    """
    Resolve um sistema triangular inferior Ly = b para y
    
    Retorna:
    y: Solução do sistema
    """
    n = L.shape[0]  # Obtém o tamanho da matriz L
    y = np.zeros(n)  # Cria um array de zeros de tamanho n
    
    for i in range(n):  # Loop pelas linhas da matriz L
        s = 0
        for j in range(i):  # Loop pelas colunas abaixo da diagonal
            s += L[i, j] * y[j]  # Calcula a soma dos termos anteriores
        y[i] = (b[i] - s)  # Calcula o valor de y[i]
    
    return y

def backward_substitution(U, y):
    """
    Resolve um sistema triangular superior Ux = y para x
    
    Retorna:
    x: Solução do sistema
    """
    n = U.shape[0]  # Obtém o tamanho da matriz U
    x = np.zeros(n)  # Cria um array de zeros de tamanho n
    
    for i in reversed(range(n)):  # Loop pelas linhas da matriz U de trás para frente
        s = 0
        for j in range(i+1, n):  # Loop pelas colunas à direita da diagonal
            s += U[i, j] * x[j]  # Calcula a soma dos termos anteriores
        x[i] = (y[i] - s) / U[i, i]  # Calcula o valor de x[i]
    
    return x