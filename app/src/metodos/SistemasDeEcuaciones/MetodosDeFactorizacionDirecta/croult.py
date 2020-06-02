from numpy import *
from sympy import *
import math
import numpy as np
L = []
U = []
Z = []
X = []

class Croult:
    def __init__(self, n, A, B):
        X.clear()
        U.clear()
        Z.clear()
        L.clear()

        self.n = n
        self.A = A
        self.B = B

    def croult(self):
        self.n = int(self.n)
    
        L = np.zeros([int(self.n), int(self.n)])
        U = np.zeros([int(self.n), int(self.n)])
        for i in range(self.n):
            U[i][i] = 1
        for k in range(self.n):
            for i in range(k,self.n):
                sum = 0
                for p in range(k):
                    sum += L[i][p]*U[p][k]
                L[i][k] = (self.A[i][k] - sum)/U[k][k]
            for j in range(k,self.n):
                sum = 0
                for p in range(k):
                    sum += L[k][p]*U[p][j]
                U[k][j] = (self.A[k][j] - sum)/L[k][k]
       
    #------------------Calcula Lz = B ----------#
        for i in range(self.n):
            sum = 0
            for j in range(i):
                sum += L[i][j]*Z[j]
            if i == 0: 
                Z.append(self.B[i]/L[i][i])
            else:
                Z.append((self.B[i]-sum)/L[i][i])
    
    #---------------Calcular Ux = B ---------#
        
        for i in range(self.n):
            
            X.append(0)
        for i in range(self.n-1,0-1,-1):
            sum = 0
            for j in range(i,self.n):
              sum += U[i][j]*X[j]
            X[i] = ((Z[i]-sum)/U[i][i])
        return(X)
        

        