from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

f = Function('fx')

def recolectarDatos():
    global f
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    x0 = input("Ingrese el primer valor inicial: ")
    x1 = input("Ingrese el segundo valor inicial: ")
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

    metodoSecante(float(x0), float(x1), float(tolerancia), niteraciones)

def metodoSecante(x0, x1, tolerancia, niteraciones):
    global f
    x = Symbol('x')
    fx0 = f.subs(x,x0)
    if fx0 == 0:
        print (str(x0) + " es una raiz")
    else:
        fx1 = f.subs(x,x1)
        cont = 0
        errorAbs = tolerancia + 1
        denominador = fx1 - fx0
        print(str(cont) + "|" + str(x0) + "|" + str(x1) + "|" + str(fx0) + "|" + str(fx1) + "\n")
        while fx1 != 0 and errorAbs > tolerancia and denominador != 0 and cont < niteraciones:
            x2 = x1 - fx1*(x1-x0)/denominador
            errorAbs = abs(x2 - x1)
            errorRel = errorAbs/x2
            x0 = x1
            fx0 = fx1
            x1 = x2
            fx1 = f.subs(x,x1)
            denominador = fx1 - fx0
            cont += 1
            print(str(cont) + "|" + str(x0) + "|" + str(x1) + "|" + str(fx0) + "|" + str(fx1) + "|" + str(errorAbs) + "|" + str(errorRel) + "\n")

        if fx1 == 0:
            print (str(x1) + " es una raiz")
        elif errorAbs < tolerancia:
            print(str(x1) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(tolerancia))
        elif denominador == 0:
            print("Hay una raiz multiple en " + str(x1))
        else:
            print("Excedio el numero de iteraciones posible")

recolectarDatos()
