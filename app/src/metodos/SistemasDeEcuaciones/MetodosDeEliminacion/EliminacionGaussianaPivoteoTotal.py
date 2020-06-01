from numpy import *
from sympy import *

class EliminacionGaussianaPivoteoTotal:
    def __init__(self, n, A):

            self.n = n
            self.A = A

    def eliminacionGaussianaPivoteoTotal(self):
        
        self.n = int(self.n)
        for k in range(1,self.n):
            
            self.A = pivoteoTotal(self.A,self.n,k-1)
            for i in range(k, self.n):
                multiplicador = float(self.A[i][k-1]/self.A[k-1][k-1])
    
                for j in range(k,self.n+2):
                    self.A[i][j-1] = self.A[i][j-1] - multiplicador*self.A[k-1][j-1]

              
        return sustitucionRegresiva(self.A,self.n)

def pivoteoTotal(A,n,k):
    mayor = 0
    filaMayor = k
    columnaMayor = k
    for r in range(k,n):
        for s in range(k,n):
            if abs(A[r][s]) > mayor:
                mayor = abs(A[r][s])
                filaMayor = r
                columnaMayor = s
    if mayor == 0:
        return ("El sistema no tiene solución única")
    else:
        if filaMayor != k:
            A = intercambieFilas(A,filaMayor,k)
        if columnaMayor != k:
            A = intercambieColumnas(A,columnaMayor,k)
           

    return A

def intercambieFilas(A,filaMayor,k):
    for i in range(len(A[0])):
        aux = A[k][i]
        A[k][i] = A[filaMayor][i]
        A[filaMayor][i] = aux
    return A

def intercambieColumnas(A,columnaMayor,k):
    for i in range(len(A[0])-1):
        aux = A[i][k]
        A[i][k] = A[i][columnaMayor]
        A[i][columnaMayor] = aux
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


