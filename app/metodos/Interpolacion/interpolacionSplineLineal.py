import numpy as np
from sympy import *
import math

def recolectarDatos():
    n = int(input("Ingrese el numero de puntos: "))
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        puntos = str(input("Ingrese los valores de x" +str(i) + ", f(x" + str(i) + ") separados por espacio: "))
        valores = puntos.split(" ")
        x[i] = float(valores[0])
        y[i] = float(valores[1])

    metodoInterpolacionSplineLineal(x, y, n)

def metodoInterpolacionSplineLineal(x, y, n):
    print("\n")
    for i in range(1,n):
        pendiente = (y[i] - y[i-1])/(x[i] - x[i-1])
        resultado = (pendiente * -x[i]) + y[i]
        print("P(X" + str(i) + ") = " + str(pendiente) + "X + " + str(resultado) + "        " + str(x[i-1]) + " <= X <= " + str(x[i]))

recolectarDatos()
