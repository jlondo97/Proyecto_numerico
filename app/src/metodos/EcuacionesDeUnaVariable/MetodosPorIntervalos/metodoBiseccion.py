from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class MetodoBiseccion:
    f = Function('fx')

    def __init__(self, xi, xs, tolerancia, iteraciones, funcion):

        self.xi = xi
        self.xs = xs
        self.tolerancia = tolerancia
        self.iteraciones = iteraciones
        self.funcion = funcion

    def metodoBiseccion(self):
        self.xi = float(self.xi) 
        self.xs = float(self.xs)
        self.tolerancia = float(self.tolerancia)
        self.iteraciones = float(self.iteraciones)
        
        f = parse_expr(self.funcion)
        x = Symbol('x')
        fxi = f.subs(x,self.xi)
        fxs = f.subs(x,self.xs)
        if fxi == 0:
            print(repr(self.xi) + " es una raiz")

        elif fxs == 0:
            print(repr(self.xs) + " es una raiz")

        elif fxi * fxs > 0:
            print("El intervalo no posee una raiz")

        else:
            xm = (self.xi + self.xs) / 2
            cont = 1
            fxm = f.subs(x,xm)
            error = self.tolerancia + 1
            while fxm != 0 and error > self.tolerancia and cont < self.iteraciones:
                if fxi * fxm < 0:
                    self.xs = xm
                    fxs = f.subs(x,self.xs)
                else:
                    self.xi = xm
                    fxi = f.subs(x,self.xi)

                xaux = xm
                xm = (self.xi + self.xs) / 2
                fxm = f.subs(x,xm)
                error = abs(xm - xaux)
                cont += 1

            if fxm == 0:
                mensaje = (repr(xm) + " es una raiz")
                return mensaje
            elif error < self.tolerancia:
                mensaje = (repr(xm) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(self.tolerancia))
                return mensaje
            else:
                mensaje = ("Excedio el numero de iteraciones posible")
                return mensaje


