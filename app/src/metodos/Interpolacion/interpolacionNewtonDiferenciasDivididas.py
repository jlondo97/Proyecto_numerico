from numpy import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

def recolectarDatos():
    n = int(input("Ingrese el numero de puntos: "))
    tabla = []
    for i in range(n):
        tabla.append([0] * (n+1))
        puntos = str(input("Ingrese los valores de x" +str(i) + ", f(x" + str(i) + ") separados por espacio: "))
        valores = puntos.split(" ")
        for j in range(2) :
            tabla[i][j] = float(valores[j])

    metodoInterpolacionNewtonDiferenciasDivididas(tabla,n)

def metodoInterpolacionNewtonDiferenciasDivididas(tabla,n):
    polinomio = "P(X) = " + str(tabla[0][1])
    F = Function('F')
    for j in range(2,n+1):
        for i in range(j-1,n):
            tabla[i][j] = (tabla[i][j-1] - tabla[i-1][j-1])/(tabla[i][0] - tabla[i-j+1][0])
            if(i==j-1):
                polinomio += " + " + str(tabla[i][j])
                for i in range(0,i):
                    polinomio += "(x - " + str(tabla[i][0]) + ")"

    imprimirTabla(tabla,n)
    F = parse_expr(polinomio.replace("P(X) = ","").replace("(","*("))
    print("\n-----------------------------------POLINOMIO INTERPOLANTE DE NEWTON CON DIFERENCIAS DIVIDIDAS --------------------------------\n \n" + "Forma esquematica: " + polinomio + "\n Forma Simplificada: P(X) = " + str(expand(F)))


def imprimirTabla(tabla,n):
    print(" n |   xi   |      f[xi]     |         primera         |          Segunda          |          Tercera          |         Cuarta         |         Quinta        |Nesima|" )
    for i in range(n):
        print(str(i) + "     " + str(tabla[i]).replace("'"," ").replace(",","       ").replace("["," ").replace("]"," ").replace(" 0 ", " "))
        print("\n")




recolectarDatos()
