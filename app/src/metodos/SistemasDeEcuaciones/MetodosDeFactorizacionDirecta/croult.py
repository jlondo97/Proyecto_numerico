from numpy import *
from sympy import *
import math

A = [] 
L = []
U = []
B = []
Z = []
X = []
n = 0
def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))
    fila = ""
    valores = []
    for i in range(n):
        A.append([0] * n)
        L.append([0] * n)
        U.append([0] * n)    
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            if j==n:
                B.append(float(valores[j]))
            else:
                A [i][j] = float(valores[j])  #Asignamos a la posicion correspondiente de la matriz los coeficientes"""
    for i in range(n):
        U[i][i] = 1
    for k in range(n):
        for i in range(k,n):
            sum = 0
            for p in range(k):
                sum += L[i][p]*U[p][k]
            L[i][k] = (A[i][k] - sum)/U[k][k]
        for j in range(k,n):
            sum = 0
            for p in range(k):
                sum += L[k][p]*U[p][j]
            U[k][j] = (A[k][j] - sum)/L[k][k]
    print("-------------------MATRIZ L -------------------------")
    printMatriz(L)
    print("-------------------MATRIZ U -------------------------")
    printMatriz(U)
    print("-------------------CALCULANDO Lz=B -------------------------")
    for i in range(n):
        sum = 0
        for j in range(i):
           sum += L[i][j]*Z[j]
        Z.append(B[i]-sum)
        print("Z"+str(i)+": "+str(Z[i]))   
    
    for i in range(n):
        X.append(0)
    for i in range(n-1,0-1,-1):
        sum = 0
        for j in range(i,n):
           sum += U[i][j]*X[j]
        X[i] = ((Z[i]-sum)/U[i][i])
    print("-------------------CALCULANDO Ux=Z -------------------------")
    for i in range(n):
        print("X"+str(i)+": "+str(X[i]))    
def printMatriz(matriz):
    for i in matriz:
        print(i)
    
recolectarDatos()
    