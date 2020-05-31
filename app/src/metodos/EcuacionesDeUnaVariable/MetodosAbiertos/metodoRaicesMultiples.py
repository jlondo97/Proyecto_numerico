from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

f = Function('fx')
df = Function('dfx')
d2f = Function('d2fx')

def recolectarDatos():
    global f
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    x0 = input("Ingrese el valor inicial: ")
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

    metodoRaicesMultiples(float(x0), float(tolerancia), niteraciones)

def metodoRaicesMultiples(x0, tolerancia, niteraciones):
    global f, df, d2f
    x = Symbol('x')
    df = diff(f,x)
    d2f = diff(df,x)
    fx = f.subs(x,x0)
    dfx = df.subs(x,x0)
    d2fx = d2f.subs(x,x0)
    cont = 0
    errorAbs = tolerancia + 1
    denominador = dfx**2 - (fx*d2fx)
    print( str(cont) + "|" + str(x0) + "|" + str(fx) + "|" + str(dfx) + "|" + str(d2fx) + "\n")
    while fx != 0 and errorAbs > tolerancia and denominador != 0 and cont < niteraciones:
        x1 = x0 - fx*dfx/denominador
        fx = f.subs(x,x1)
        dfx = df.subs(x,x1)
        d2fx = d2fx.subs(x,x1)
        errorAbs = abs(x1 - x0)
        errorRel = errorAbs/x1
        x0 = x1
        cont += 1
        print(str(cont) + "|" + str(x0) + "|" + str(fx) + "|" + str(dfx) + "|" + str(d2fx) + "|" + str(errorAbs) + "|" + str(errorRel) + "\n")

    if fx == 0:
        print (str(x0) + " es una raiz")
    elif errorAbs < tolerancia:
        print(str(x0) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(tolerancia))
    elif dfx == 0:
        print(str(x0) + " Es una raiz multiple simple")
    elif d2fx == 0:
        print(str(x0) + " Es una raiz multiple de multiplicidad 2")
    else:
        print("Excedio el numero de iteraciones posible")

recolectarDatos()
