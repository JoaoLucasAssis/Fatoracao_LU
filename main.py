import numpy as np
from lu_decomposition import lu_decomposition
from substitution import forward_substitution, backward_substitution

def read_matrix_file(path):
    A = []
    with open(path, 'r') as file:
        for line in file:
            row = list(map(float, line.strip().split()))
            A.append(row)
    return np.array(A)

def main():
    path = 'matrix.txt'

    b = [11, -16, 17]
    
    A = read_matrix_file(path)

    if A.shape[0] == A.shape[1]:
        L, U = lu_decomposition(A)
        y = forward_substitution(L, b)
        x = backward_substitution(U, y)
        print("Solução:", x)
        
if __name__ == "__main__":
    main()