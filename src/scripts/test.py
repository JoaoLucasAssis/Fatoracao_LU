import numpy as np
from scipy.linalg import solve_triangular

A = np.array([[4, -2, 1], [-2, 4, -2], [1, -2, 4]])
U = np.array([[4, -2, 1], [0, 3, -1.5], [0, 0, 3]])
L = np.array([[1, 0, 0], [-0.5, 1, 0], [0.25, -0.5, 1]])
b = np.array([11, -16, 17])

def solve():
    x = np.linalg.solve(A, b)
    print("Solução completa:", x)

def lu_decomposition():
    y = solve_triangular(L, b, lower=True)
    x = solve_triangular(U, y, lower=False)
    print("Solução x (substituição regressiva):", x)

solve()
lu_decomposition()