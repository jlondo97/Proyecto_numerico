from numpy import *
from sympy import *


class EliminacionGaussianaSimple:

    def __init__(self, n, A):

        self.n = n
        self.A = A

    def eliminacionGaussianaSimple(self):
       # print("\n    MATRIZ ORIGINAL A")
       # imprimirMatriz(A,n)
        self.n = int(self.n)
        for k in range(1,self.n):
            #print("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(A[k-1][k-1]) + "\n")
            for i in range(k, self.n):
                multiplicador = float(self.A[i][k-1]/self.A[k-1][k-1])
                #print("\nM" + str(i) + str(k) + " = " + str(multiplicador))
                for j in range(k,self.n+2):
                    self.A[i][j-1] = self.A[i][j-1] - multiplicador*self.A[k-1][j-1]
        x = []
        for i in range(self.n):
            x.append([0])

        for i in range(self.n,0,-1):
            sumatoria = 0
            for p in range(i+1, self.n+1, 1):
                sumatoria += self.A[i-1][p-1]*x[p-1]
            x[i-1] = (self.A[i-1][self.n] - sumatoria)/ self.A[i-1][i-1]
       
        return(x)
                
        
        

    # def sustitucionRegresiva(self):
    #     self.n = int(self.n)
    #     x = []
    #     for i in range(self.n):
    #         x.append([0])

    #     for i in range(self.n,0,-1):
    #         sumatoria = 0
    #         for p in range(i+1, self.n+1, 1):
    #             sumatoria += self.A[i-1][p-1]*x[p-1]
    #         x[i-1] = (self.A[i-1][self.n] - sumatoria)/ self.A[i-1][i-1]
       
    #     return(x)


