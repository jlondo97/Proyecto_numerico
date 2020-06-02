import numpy as np
from sympy import *
import sys
import math

A = []
L = []
U = []
B = []
Y = []
X = []

def inputYverificacion():

    n = int(input("Ingrese el numero de ecuaciones: "))  #Conociendo el numero de ecuaciones, conoceremos las dimensiones de la matriz
    A = []  

    for i in range(n):
        A.append([0] * (n))    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n):       #Es n+1 por la columna de terminos independientes
            A [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes

    B = [0] * (n)
    columnas = str(input("Ingrese los valores de B separados por espacio: "))
    val = columnas.split(" ")
    print(B)
    for j in range(n):
        B[j] = float(val[j])
    print(B)

    for i in range(n):
        L.append([])
        U.append([])
        for j in range(n):
            L[i].append(0)
            U[i].append(0)

    conversionL(A, L, U, B, n)
    
def imprimirMatriz(l, U, n):
    print("Matriz L")
    for i in range(n):
        print(str(L[i]).replace("'"," ").replace(","," "))
    print(" ")
    print("Matriz U")
    for i in range(n):
        print(str(U[i]).replace("'"," ").replace(","," "))



def resolverMatriz(L,U,B,n):
    
    Y =  [0] * n
    X = [0] * n
    print(" ")
    print("Y")
    print(Y)
    for p in range(n):
        for k in range(n):
            if k == 0 and p == 0:
                Ymn = B[k] / L[k][p]
                Y[k] = Ymn
            elif k == p:
                Ymn = B[k]
                for t in range(k):
                    Ymn = Ymn - Y[t]*L[k][t]                 
                Ymn = Ymn / L[k][p]
                Y[k] = Ymn
    print(" ")
    print("Y")
    print(Y)

    for p in range(n-1,-1,-1):
        for k in range(n-1,-1,-1):
            if k == 3 and p == 3:
                Xmn = Y[k] / U[k][p]
                X[k] = Xmn                
            elif k == p:
                Xmn = Y[k]
                for t in range(1,4):                    
                    Xmn = Xmn - X[t]*U[k][t]               
                Xmn = Xmn / U[k][p]
                X[k] = Xmn
    print(" ")
    print("X")
    print(X)


def conversionL(A,L,U,B,n):

    for y in range(n):        
        for x in range(n):              
            if y == x:
                if y == 0:
                    Lmn = float(math.sqrt(A[x][y]))
                    L[x][y] = Lmn 
                    U[x][y] = Lmn
                else:
                    Umn = A[x][y]
                    for t in range(y):
                        Umn = Umn - L[x][t]*U[t][x]                        
                    Umn = float(math.sqrt(Umn))
                    L[x][y] = Umn
                    U[x][y] = Umn


            elif x > y:
                if y == 0:
                    Lxy = A[x][y] / Lmn
                    L[x][y] = Lxy
                else:
                    Lxy = A[x][y]
                    for t in range(y):
                        Lxy = Lxy - L[x][t]*U[t][y]
                    
                    Lxy = Lxy / U[y][y]
                    L[x][y] = Lxy


            elif y > x:
                if x == 0:
                    Uxy = A[x][y] / Lmn
                    U[x][y] = Uxy
                else:
                    Uxy = A[x][y]
                    for t in range(y):
                        Uxy = Uxy - L[x][t]*U[t][y]
                    Uxy = Uxy / L[x][x]
                    U[x][y] = Uxy         
    
    imprimirMatriz(L,U,n)
    resolverMatriz(L,U,B,n)

inputYverificacion()

