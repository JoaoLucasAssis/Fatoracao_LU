import numpy as np
from scripts.lu_decomposition import lu_decomposition
from scripts.substitution import forward_substitution, backward_substitution
 
def valid_matrix_file(A):
    if not A:
        print("O arquivo 'matrix.txt' está vazio.")
        raise SystemExit
    
    for row in A:
        if(len(row) != len(A[0])): # Verifica se cada linha tem o mesmo número de colunas da matriz
            print("Matriz inválida. A matriz deve ter o mesmo número de linhas e colunas.")
            raise SystemExit
    
    return np.array(A)

def valid_vector_file(b, n):
    if not b:
        print("O arquivo 'matrix.txt' está vazio.")
        raise SystemExit
    elif len(b) != n: # Verifica se o vetor tem o mesmo número de linhas da matriz
        print("Vetor inválido. O vetor deve ter o mesmo número de linhas da matriz.")
        raise SystemExit
    else:
        return np.array(b)

def read_matrix_file(path):
    A = []
    with open(path, 'r') as file:
        try: 
            for line in file:
                row = list(map(float, line.strip().split()))
                A.append(row)
        except ValueError:
            print("Erro ao ler o arquivo 'matrix.txt'. Digite apenas números inteiros ou racionais.")
            raise SystemExit
    return A

def read_vector_file(path):
    b = []
    with open(path, 'r') as file:
        try:
            for line in file:
                n = float(line.strip())
                b.append(n)
        except ValueError:
            print("Erro ao ler o arquivo 'b.txt'. O vetor deve ter apenas uma coluna.")
            raise SystemExit
        
    return b

def main():
    matrix_path = 'matrix.txt'
    vector_path = 'b.txt'
    
    A = read_matrix_file(matrix_path)
    A = valid_matrix_file(A)
    b = read_vector_file(vector_path)
    b = valid_vector_file(b, len(A))

    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)

    print("Solução:", x)
        
if __name__ == "__main__":
    main()