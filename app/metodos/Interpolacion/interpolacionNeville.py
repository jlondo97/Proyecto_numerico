from numpy import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

def recolectarDatos():
    n = int(input("Ingrese el numero de puntos: "))
    x0 = float(input("Ingrese el X: "))
    tabla = []
    for i in range(n):
        tabla.append([0] * (n+1))
        puntos = str(input("Ingrese los valores de x" +str(i) + ", f(x" + str(i) + ") separados por espacio: "))
        valores = puntos.split(" ")
        for j in range(2) :
            tabla[i][j] = float(valores[j])

    metodoInterpolacionNeville(tabla,n,x0)

def metodoInterpolacionNeville(tabla,n,x0):
    F = Function('F')
    x = Symbol('x')
    for j in range(2,n+1):
        for i in range(j-1,n):
           xi = tabla[i-j+1][0]
           xj = tabla[i][0]
           pui = tabla[i-1][j-1]
           pj = tabla[i][j-1]
           F = ((x-xi)*pj-(x-xj)*pui)/(xj - xi)
           tabla[i][j] = F.subs(x,x0)

    imprimirTabla(tabla,n)
    print("\n-----------------------------------POLINOMIO INTERPOLANTE DE NEWTON CON DIFERENCIAS DIVIDIDAS --------------------------------\n \n" + "Forma esquematica: " + str(tabla[n-1][n]) + "\n Forma Simplificada: P(X) = " + str(expand(F)))


def imprimirTabla(tabla,n):
    print(" n |   xi   |      f[xi]     |         primera         |          Segunda          |          Tercera          |         Cuarta         |         Quinta        |Nesima|" )
    for i in range(n):
        print(str(i) + "     " + str(tabla[i]).replace("'"," ").replace(",","       ").replace("["," ").replace("]"," ").replace(" 0 ", " "))
        print("\n")




recolectarDatos()
