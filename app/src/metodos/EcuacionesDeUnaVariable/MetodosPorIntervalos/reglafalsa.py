from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


class ReglaFalsa:

    f = Function('fx')

    def __init__(self, xi, xs, tolerancia, iteraciones, funcion):

        self.xi = xi
        self.xs = xs
        self.tolerancia = tolerancia
        self.iteraciones = iteraciones
        self.funcion = funcion
        self.vector = []

    def metodoReglaFalsa(self):

        self.xi = float(self.xi)
        self.xs = float(self.xs)
        self.tolerancia = float(self.tolerancia)
        self.iteraciones = float(self.iteraciones)

        f = parse_expr(self.funcion)
        x = Symbol('x')
        fxi = f.subs(x, self.xi)
        fxs = f.subs(x, self.xs)
        if fxi == 0:
            mensaje = (repr(self.xi) + " es una raiz")
            return mensaje

        elif fxs == 0:
            mensaje = (repr(self.xs) + " es una raiz")

        elif fxi * fxs < 0:
            xm = self.xi - (fxi) * (self.xi - self.xs) / (fxi - fxs)
            fxm = f.subs(x, xm)
            contador = 1
            error = self.tolerancia + 1
            self.vector.append([str(contador), str(self.xs), str(
                xm), str(self.xi), str(fxm), str(error)])
            while(fxm != 0 and error > self.tolerancia and contador < self.iteraciones):
                if(fxi * fxm < 0):
                    self.xs = xm
                    fxs = f.subs(x, self.xs)
                    self.vector.append([str(contador), str(self.xs), str(
                        xm), str(self.xi), str(fxm), str(error)])
                else:
                    self.xi = xm
                    fxi = f.subs(x, self.xi)
                xaux = xm
                xm = self.xi - (fxi) * (self.xi - self.xs) / (fxi - fxs)
                fxm = f.subs(x, xm)
                error = abs(xm - xaux)
                contador = contador + 1
                self.vector.append([str(contador), str(self.xs), str(
                    xm), str(self.xi), str(fxm), str(error)])
            if(fxm == 0):
                mensaje = (repr(xm) + " es una raiz")
                return mensaje
            elif(error < self.tolerancia):
                mensaje = (repr(
                    xm) + " se aproxima a una raíz de la función con una tolerancia de: " + str(repr(self.tolerancia)))
                return mensaje
            else:
                mensaje = ("No se encontro raiz con esa aproximación")
                return mensaje
        else:
            mensaje = (
                "El intervalo no cumple con las condiciones para buscar una raíz")
            return mensaje
