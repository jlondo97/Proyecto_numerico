from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

f = Function('fx')

def recolectarDatos():
    global f
    f = parse_expr(input("Ingrese la función f(x) a ser evaluada: "))
    print("La función es: " + str(f))
    xi = input("Ingrese el extremo inferior: ")
    xs = input("Ingrese el extremo superior: ")
    tolerancia = input("Ingrese la tolerancia: ")
    while (tolerancia == 0):
        print("La tolerancia debe ser diferente de 0, ingresela nuevamente")
        tolerancia = input("Ingrese la tolerancia: ")

    niteraciones = int(input("Ingrese el numero maximo de iteraciones: "))
    while (niteraciones<0):
        print("El numero de iteraciones debe ser mayor que 0, ingreselo nuevamente")
        niteraciones = int(input("Ingrese el numero máximo de iteraciones: "))

    metodoBiseccion(float(xi),float(xs),float(tolerancia),niteraciones)

def metodoBiseccion(xi,xs,tolerancia, niteraciones):
    global f
    x = Symbol('x')
    fxi = f.subs(x,xi)
    fxs = f.subs(x,xs)
    if fxi == 0:
        print(repr(xi) + " es una raiz")

    elif fxs == 0:
        print(repr(xs) + " es una raiz")

    elif fxi * fxs > 0:
        print("El intervalo no posee una raiz")

    else:
        xm = (xi + xs) / 2
        cont = 1
        fxm = f.subs(x,xm)
        error = tolerancia + 1
        while fxm != 0 and error > tolerancia and cont < niteraciones:
            if fxi * fxm < 0:
                xs = xm
                fxs = f.subs(x,xs)
            else:
                xi = xm
                fxi = f.subs(x,xi)

            xaux = xm
            xm = (xi + xs) / 2
            fxm = f.subs(x,xm)
            error = abs(xm - xaux)
            cont += 1

        if fxm == 0:
            print (repr(xm) + " es una raiz")
        elif error < tolerancia:
            print(repr(xm) + " se aproxima a una raiz de la función, con una tolerancia de: " + tolerancia)
        else:
            print("Excedio el numero de iteraciones posible")

recolectarDatos()
