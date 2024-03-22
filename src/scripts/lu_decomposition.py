import numpy as np

def lu_decomposition(A):
    """
    Executa a fatoração LU de uma matriz A
    
    Retorna:
    L: Matriz triangular inferior
    U: Matriz triangular superior
    """
    n = A.shape[0]  # Obtém o tamanho da matriz A
    L = np.eye(n)   # Inicializa L como a matriz identidade
    U = A.copy()    # Inicializa U como uma cópia da matriz A
    
    for i in range(n-1):  # Loop pelas colunas, exceto a última
        for j in range(i+1, n):  # Loop pelas linhas abaixo da diagonal
            pivot = U[j, i] / U[i, i]  # Calcula o pivot
            L[j, i] = pivot  # Adiciona o pivot a matriz triangular inferior
            for k in range(i, n):  # Atualiza os elementos da linha
                U[j, k] -= pivot * U[i, k]
    
    return L, U
