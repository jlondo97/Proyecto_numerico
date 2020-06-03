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
        self.vector = []
        self.valores = []

    def metodoBiseccion(self):
        self.xi = float(self.xi)
        self.xs = float(self.xs)
        self.tolerancia = float(self.tolerancia)
        self.iteraciones = float(self.iteraciones)

        f = parse_expr(self.funcion)
        x = Symbol('x')
        self.valores.append([10, 20, 30, 40])
        fxi = f.subs(x, self.xi)
        fxs = f.subs(x, self.xs)
        if fxi == 0:
            mensaje = (repr(self.xi) + " es una raiz")
            return mensaje

        elif fxs == 0:
            mensaje = (repr(self.xs) + " es una raiz")
            return mensaje

        elif fxi * fxs > 0:
            mensaje = ("El intervalo no posee una raiz")
            return mensaje

        else:
            xm = (self.xi + self.xs) / 2
            cont = 1
            fxm = f.subs(x, xm)
            error = self.tolerancia + 1
            self.vector.append([str(cont), str(self.xs), str(
                xm), str(self.xi), str(fxm), str(error)])
            while fxm != 0 and error > self.tolerancia and cont < self.iteraciones:
                if fxi * fxm < 0:
                    self.xs = xm
                    fxs = f.subs(x, self.xs)
                    self.vector.append([str(cont), str(self.xs), str(
                        xm), str(self.xi), str(fxm), str(error)])
                else:

                    self.xi = xm
                    fxi = f.subs(x, self.xi)

                xaux = xm
                xm = (self.xi + self.xs) / 2
                fxm = f.subs(x, xm)
                error = abs(xm - xaux)
                cont += 1
                self.vector.append([str(cont), str(self.xs), str(
                    xm), str(self.xi), str(fxm), str(error)])

            if fxm == 0:
                mensaje = (repr(xm) + " es una raiz")
                return mensaje
            elif error < self.tolerancia:
                mensaje = (repr(
                    xm) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(self.tolerancia))
                return mensaje
            else:
                mensaje = ("Excedio el numero de iteraciones posible")
                return mensaje
