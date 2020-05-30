from numpy import *
from sympy import *
import math

def recolectarDatos():
    n = int(input("Ingrese el numero de ecuaciones: "))
    tolerancia = float(input("Ingrese la tolerancia: "))
    niter = int(input("Ingrese el numero maximo de iteraciones: "))
    omega = float(input("Ingrese el valor de omega: "))
    A = []   #En primera instacia creamos una lista que posteriormente se convertira en una matriz
    x0 = [] #Lista de los valores inciales de la variables
    b = [] #Vector de terminos independientes
    for i in range(n):
        A.append([0] * n)    #Se le agregan n+1 columnas a la matriz por los terminos independientes
        fila = str(input("Ingrese los valores de la fila " + str(i+1) + " separados por espacio: "))  #El usuario ingresa los coeficientes de la matriz
        valores = fila.split(" ")
        for j in range(n+1):       #Es n+1 por la columna de terminos independientes
            if j==n:
                b.append(float(valores[j]))
            else:
                A [i][j] = float(valores[j])  #Asignamos a la posición correspondiente de la matriz los coeficientes

    for i in range(n):
        inicial = float(input("Ingrese el valor inicial de X" + str(i+1) + ": "))
        x0.append(inicial)

    metodoJacobiConRelajacion(A, b, n, x0, niter,tolerancia,omega)

def metodoJacobiConRelajacion(A, b, n, x0, niter, tolerancia,omega):
    contador = 0
    dispersion = tolerancia + 1
    x1 = []
    print("\nOrden de los datos: n, x1, x2, x3, ... xn, dispersion " )
    print(str(contador) + "    " + str(x0) + "\n")
    while dispersion > tolerancia and contador < niter:
        x1 = calcularNuevoJacobi(x0, n, b, A, omega)
        dispersion = normaEuclidiana(x1, x0,n)
        x0 = x1
        contador += 1
        print(str(contador) + "   " + str(x0) + "   " + str(dispersion) + "\n")

    if dispersion < tolerancia:
        print(str(x1) + " es una aproximación con una tolerancia: " + str(tolerancia))
    else:
        print("Fracaso en " + str(niter) + " iteraciones")


def calcularNuevoJacobi(x0, n, b, A, omega):
    x1 = []
    for i in range(n):
        suma = 0.0
        for j in range(n):
            if j != i:
                valor = x0.pop(j)
                x0.insert(j,valor)
                suma += A[i][j] * valor

        valor = b.pop(i)
        original = x0.pop(i)
        x0.insert(i,original)
        b.insert(i,valor)
        elemento = (valor - suma)/A[i][i]
        relajado = omega * elemento + (1 - omega) * original
        x1.append(relajado)

    return x1

def normaEuclidiana(x1, x0, n):
    norma = 0
    sumaCuadrados = 0
    for i in range(n):
        valor0 = x0.pop(i)
        valor1 = x1.pop(i)
        x0.insert(i,valor0)
        x1.insert(i,valor1)
        sumaCuadrados += (valor1-valor0)**2

    norma = sqrt(sumaCuadrados)
    return norma

recolectarDatos()
