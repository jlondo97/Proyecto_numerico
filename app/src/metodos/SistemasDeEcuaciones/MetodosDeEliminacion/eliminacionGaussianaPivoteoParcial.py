from numpy import *
from sympy import *

class EliminacionGaussianaPivoteoParcial:

    def __init__(self, n, A):

            self.n = n
            self.A = A

    def eliminacionGaussianaPivoteoParcial(self):
        self.n = int(self.n)
    
        for k in range(1,self.n):
    
            self.A = pivoteoParcial(self.A,self.n,k-1)
           
            for i in range(k, self.n):
                multiplicador = float(self.A[i][k-1]/self.A[k-1][k-1])
                for j in range(k,self.n+2):
                    self.A[i][j-1] = self.A[i][j-1] - multiplicador*self.A[k-1][j-1]

        return sustitucionRegresiva(self.A,self.n)


def pivoteoParcial(A,n,k):
    mayor = abs(A[k][k])
    filaMayor = k
    for s in range(k+1,n):
        if abs(A[s][k]) > mayor:
            mayor = abs(A[s][k])
            filaMayor = s
    if mayor == 0:
        return ("El sistema no tiene solución única")
    else:
        if filaMayor != k:
            A = intercambieFilas(A,filaMayor,k)
        return A

def intercambieFilas(A,filaMayor,k):
    for i in range(len(A[0])):
        aux = A[k][i]
        A[k][i] = A[filaMayor][i]
        A[filaMayor][i] = aux
    return A

def sustitucionRegresiva(A,n):
    x = []
    for i in range(n):
        x.append([0])
    for i in range(n,0,-1):
        sumatoria = 0
        for p in range(i+1, n+1, 1):
            sumatoria += A[i-1][p-1]*x[p-1]
        x[i-1] = (A[i-1][n] - sumatoria)/ A[i-1][i-1]
    return(x)
   
