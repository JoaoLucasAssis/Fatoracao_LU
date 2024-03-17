import numpy as np

def forward_substitution(L, b):
    """
    Resolve um sistema triangular inferior Ly = b para y
    
    Retorna:
    y: Solução do sistema
    """
    n = L.shape[0]
    y = np.zeros(n) # Cria um array de zeros de tamanho n

    for i in range(n):
        s = 0
        for j in range(i):
            s += L[i, j] * y[j]
        y[i] = (b[i] - s) / L[i, i]
        
    return y

def backward_substitution(U, y):
    """
    Resolve um sistema triangular superior Ux = y para x
    
    Retorna:
    x: Solução do sistema
    """
    n = U.shape[0]
    x = np.zeros(n) # Cria um array de zeros de tamanho n

    for i in reversed(range(n)):
        s = 0
        for j in range(i+1, n):
            s += U[i, j] * x[j]
        x[i] = (y[i] - s) / U[i, i]
        
    return x