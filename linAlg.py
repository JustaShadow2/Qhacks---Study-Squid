import random
import numpy as np
from sympy.matrices import Matrix

def NewMatrix():
    m = random.randint(2, 5)
    isSquare = bool(random.getrandbits(1))
    if isSquare:
        n = m
        matrix = np.random.randint(0, 9, (m, n))
        x = RREF(matrix)
    else:
        n = m + 1
        matrix = np.random.randint(0, 9, (m, n))
        x = Augmented(n, matrix)
    solution = np.array(x)
    return isSquare, matrix, solution
def RREF(matrix):
    xunsolved = Matrix(matrix)
    x = Matrix.echelon_form(xunsolved)
    return x
def Augmented(n, matrix):
    A = Matrix(np.delete(matrix, n - 1, 1))
    b = Matrix(matrix[:, n - 1])
    x = A.LUsolve(b)
    return x