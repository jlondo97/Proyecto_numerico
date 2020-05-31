from numpy import *
from sympy import *

def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))  #Conociendo el numero de ecuaciones, conoceremos las dimensiones de la matriz
    A = []   #En primera instacia creamos una lista que posteriormente se convertira en una matriz
    for i in range(n):
        A.append([0] * (n+1))    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            A [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes

    eliminacionGaussianaSimple(A, n)

def eliminacionGaussianaSimple(A,n):
    print("\n    MATRIZ ORIGINAL A")
    imprimirMatriz(A,n)
    for k in range(1,n):
        #print("\nETAPA " + str(k) + "\nObjetivo: Poner ceros bajo el elemento A" + str(k) + str(k) + " = " + str(A[k-1][k-1]) + "\n")
        for i in range(k, n):
            multiplicador = float(A[i][k-1]/A[k-1][k-1])
            #print("\nM" + str(i) + str(k) + " = " + str(multiplicador))
            for j in range(k,n+2):
                A[i][j-1] = A[i][j-1] - multiplicador*A[k-1][j-1]

            #imprimirMatriz(A,n)
    print("\n   MATRIZ TRIANGULAR SUPERIOR\n")
    imprimirMatriz(A,n)
    sustitucionRegresiva(A,n)

def sustitucionRegresiva(A,n):
    print("\n SUSTITUCIÓN REGRESIVA\n")
    x = []
    for i in range(n):
        x.append([0])

    for i in range(n,0,-1):
        sumatoria = 0
        for p in range(i+1, n+1, 1):
            sumatoria += A[i-1][p-1]*x[p-1]
        x[i-1] = (A[i-1][n] - sumatoria)/ A[i-1][i-1]
        print("X" + str(i) + " = " + str(x[i-1]))


def imprimirMatriz(A, n):
    for i in range(n):
        print(str(A[i]).replace("'"," ").replace(","," "))

recolectarDatos()
