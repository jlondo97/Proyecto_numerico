from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


class PuntoFijo:

    f = Function('fx')
    g = Function('gx')

    def __init__(self, xa, tolerancia, iteraciones, f, g):
        self.xa = xa
        self.tolerancia = tolerancia
        self.iteraciones = iteraciones
        self.f = f
        self.g = g
        self.vector = []

    def metodoPuntoFijo(self):

        self.xa = float(self.xa)
        self.tolerancia = float(self.tolerancia)
        self.iteraciones = float(self.iteraciones)

        f = parse_expr(self.f)
        g = parse_expr(self.g)

        x = Symbol('x')
        fx = f.subs(x, self.xa)

        cont = 0
        errorAbs = self.tolerancia + 1
        self.vector.append(
            [str(cont), str(self.xa), str(fx), str(errorAbs)])
        while fx != 0 and errorAbs > self.tolerancia and cont < self.iteraciones:
            xn = g.subs(x, self.xa)
            xn = float(xn)
            fx = f.subs(x, xn)
            errorAbs = abs(xn - self.xa)

            self.xa = xn
            cont += 1
            self.vector.append(
                [str(cont), str(xn), str(fx), str(errorAbs)])

        if fx == 0:
            mensaje = (str(self.xa) + " es una raiz")
            return mensaje
        elif errorAbs < self.tolerancia:
            mensaje = (str(
                self.xa) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(self.tolerancia))
            return mensaje
        else:
            mensaje = ("No hay raiz con esos parametros")
            return mensaje
