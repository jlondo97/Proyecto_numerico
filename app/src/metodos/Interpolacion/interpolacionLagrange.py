import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
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

    metodoInterpolacionLagrange(x, y, n)

def metodoInterpolacionLagrange(x, y, n):
    polinomio = ""
    F = Function('F')
    G = Function('G')
    print("\n----------------------------FORMA ESQUEMATICA POLINOMIO DE LAGRANGE---------------------------\n\n----------------- P(X) = L0(X)F(X0) + L1(X)F(X1) + L2(X)F(X2) + ... + LN(X)F(XN)---------------")
    for i in range(n):
        L = "("
        for j in range(n):
            if (j != i):
                L += "(x - " + str(x[j]) + ")"
        L += ")"
        L += " / ("
        for j in range(n):
            if (j != i):
                L += "(" + str(x[i]) + " - " + str(x[j]) + ")"

        L += ")"
        L = L.replace(")(",")*(")
        F = parse_expr(L)
        print("\n L" + str(i) + "(x) = " + L.replace("((","(").replace("))",")") + " = " + str(expand(F)))
        toReplace = "L" + str(i) + "(x) = "
        if i == n-1:
            polinomio += "(" + str(expand(F)) + ")*" + str(y[i])
        else:
            polinomio += "(" + str(expand(F)) + ")*" + str(y[i]) + " + "

    G = str(expand(polinomio))


    print("\n-----------------------------------POLINOMIO INTERPOLANTE DE LAGRANGE --------------------------------\n \n" + "P(X) = " + G)








recolectarDatos()
