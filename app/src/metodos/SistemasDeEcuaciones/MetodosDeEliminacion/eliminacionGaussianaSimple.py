from numpy import *
from sympy import *


class EliminacionGaussianaSimple:

    def __init__(self, n, A):

        self.n = n
        self.A = A
        self.vector = []

    def eliminacionGaussianaSimple(self):
        print("\n    MATRIZ ORIGINAL A")
        print(self.A)
        self.n = int(self.n)
        for k in range(1, self.n):
            print("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" +
                  str(k) + str(k) + " = " + str(self.A[k-1][k-1]) + "\n")
            for i in range(k, self.n):
                multiplicador = float(self.A[i][k-1]/self.A[k-1][k-1])
                print("\nM" + str(i) + str(k) + " = " + str(multiplicador))
                # self.vector.append(str(multiplicador))
                for j in range(k, self.n+2):
                    self.A[i][j-1] = self.A[i][j-1] - \
                        multiplicador*self.A[k-1][j-1]

        return sustitucionRegresiva(self.A, self.n)


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
