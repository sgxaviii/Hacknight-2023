import numpy as np

def is_even(p):

    if len(p) == 1:
        return True

    trans = 0

    for i in range(0,len(p)):
        j = i + 1

        for j in range(j, len(p)):
            if p[i] > p[j]: 
                trans = trans + 1

    return ((trans % 2) == 0)

def matriu_random(n, m):
    llista = np.arange(0, (n*m), 1)
    vec = np.random.permutation(llista)
    while (is_even(vec)):
        vec = np.random.permutation(llista)
    A = np.zeros((n,m))
    for i in range (n):
        A[i] = vec[i*m:(i+1)*m]
    return A

def matriu_guanyadora(n,m):
    llista = np.arange(0, (n*m), 1)
    A = np.zeros((n,m))
    for i in range(n):
        A[i] = llista[i*m:(i+1)*m]
    
    return A

def trobar_zero(A):
    res = np.where(A==0)
    resultat = np.array([res[0][0], res[1][0]])
    return resultat

A = matriu_random(3, 3)
print(A)
print(trobar_zero(A))