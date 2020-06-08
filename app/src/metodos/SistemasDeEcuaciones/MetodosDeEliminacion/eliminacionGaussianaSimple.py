from numpy import *
from sympy import *


class EliminacionGaussianaSimple:

    def __init__(self, n, A):

        self.n = n
        self.A = A
        self.vector = []
        self.matrices = []
        self.objetivos = []
        self.multiplicadores = []
    def eliminacionGaussianaSimple(self):
        # print("\n    MATRIZ ORIGINAL A")
        # print(self.A)
        self.n = int(self.n)
        A2 = self.A
        for k in range(1, self.n):
            self.objetivos.append(" ETAPA " + str(k) + " Objetivo: Poner ceros bajo el elemento A" +
                  str(k) + str(k) + " = " + str(A2[k-1][k-1]))
            for i in range(k, self.n):
                multiplicador = float(A2[i][k-1]/A2[k-1][k-1])
                self.multiplicadores.append("M" + str(i) + str(k) + " = " + str(multiplicador))

                for j in range(k, self.n+2):
                    A2[i][j-1] = A2[i][j-1] - multiplicador*A2[k-1][j-1]
                    
                self.matrices.append(str(A2))
                
        #self.objetivos.append("   MATRIZ TRIANGULAR SUPERIOR")
        #self.matrices.append(self.A)   
        # print(self.objetivos)
        # print(self.multiplicadores)
        # print(self.matrices)
        return sustitucionRegresiva(A2, self.n)


def sustitucionRegresiva(A, n):
    x = []
    for i in range(n):
        x.append([0])

    for i in range(n, 0, -1):
        sumatoria = 0
        for p in range(i+1, n+1, 1):
            sumatoria += A[i-1][p-1]*x[p-1]
        x[i-1] = (A[i-1][n] - sumatoria) / A[i-1][i-1]
    return(x)
