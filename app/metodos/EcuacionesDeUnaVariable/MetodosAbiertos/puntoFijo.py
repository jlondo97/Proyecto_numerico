from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

f = Function('fx')
g = Function('gx')

def recolectarDatos():
    global f,g
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    g = parse_expr(input("Ingrese la función g(x) a ser evaluada: "))
    xa = input("Ingrese la aproximación inicial: ")
    tolerancia = input("Ingrese la tolerancia: ")
    print("La tolerancia es: " + str(tolerancia))
    while (tolerancia == 0):
        print("La tolerancia debe ser diferente de 0, ingresela nuevamente")
        tolerancia = input("Ingrese la tolerancia: ")

    niteraciones = int(input("Ingrese el numero maximo de iteraciones: " ))
    print("\n")

    while (niteraciones<0):
        print("El numero de iteraciones debe ser mayor que 0, ingreselo nuevamente")
        niteraciones = int(input("Ingrese el numero máximo de iteraciones: "))

    metodoPuntoFijo(float(xa), float(tolerancia), niteraciones)

def metodoPuntoFijo(xa, tolerancia, niteraciones):
    global f,g
    x = Symbol('x')
    fx = f.subs(x,xa)
    cont = 0
    print( str(cont) + "|" + str(xa) + "|" + str(fx) + "\n")
    errorAbs = tolerancia + 1
    while fx != 0 and errorAbs > tolerancia and cont < niteraciones:
        xn = g.subs(x,xa)
        fx = f.subs(x,xn)
        errorAbs = abs(xn - xa)
        errorRel = errorAbs/xn
        xa = xn
        cont += 1
        print(str(cont) + "|" + str(xa) + "|" + str(fx) + "|" + str(errorAbs) + "|" + str(errorRel) + "\n")

    if fx == 0:
        print (str(xa) + " es una raiz")
    elif errorAbs < tolerancia:
        print(str(xa) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(tolerancia))
    else:
        print("Excedio el numero de iteraciones posible")

recolectarDatos()
