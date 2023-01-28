import random

def Matrix(min, max, isSquare, isAugmented):
    #Todo:
        #Implement augmented matrices
        #Implement non-square matrices
    #Current State:
        #Basically just makes matrices that are easy to RREF
    #min = 2
    #max = 5
    n = random.randint(min, max)
    #isSquare = True
    #isAugmented = False
    if (isSquare):
        m = n
    else:
        while (m == n):
            m = random.randint(min, max)
    if (isAugmented and (isSquare == False)): 
        m = m + 1 #m + 1 matrices so we have augmented stuff woo
    x = [[0 for i in range(n)] for j in range(m)] # x is now a 10x10 array of 0
    for i in range(n-1):
        for j in range (m-1):
            x[i][j] = random.randint()
            if (i >= 1):
                while (x[i][j] % x[i-1][j] != 0):
                    x[i][j] = random.randint()
    return x #passes back the matrix