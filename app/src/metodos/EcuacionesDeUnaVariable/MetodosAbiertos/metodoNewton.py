from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

class MetodoNewton:
    f = Function('fx')
    df = Function('dfx')

    def __init__(self, x0, tolerancia, iteraciones, f):
        self.x0 = x0
        self.iteraciones = iteraciones
        self.tolerancia = tolerancia
        self.f = f

    def metodoNewton(self):

        self.x0 = float(self.x0)
        self.tolerancia = float(self.tolerancia)
        self.iteraciones = float(self.iteraciones)

        f = parse_expr(self.f)

        x = Symbol('x')
        df = diff(f, x)
        fx = f.subs(x, self.x0)
        dfx = df.subs(x, self.x0)
        cont = 0
        errorAbs = self.tolerancia + 1
        #print( str(cont) + "|" + str(x0) + "|" + str(fx) + "|" + str(dfx) + "\n")
        while fx != 0 and errorAbs > self.tolerancia and dfx != 0 and cont < self.iteraciones:
            x1 = self.x0 - fx/dfx
            fx = f.subs(x, x1)
            dfx = df.subs(x, x1)
            errorAbs = abs(x1 - self.x0)
            errorRel = errorAbs/x1
            self.x0 = x1
            cont += 1
            #print(str(cont) + "|" + str(x0) + "|" + str(fx) + "|" + str(dfx) + "|" + str(errorAbs) + "|" + str(errorRel) + "\n")

        if fx == 0:
            return (str(self.x0) + " es una raiz")
        elif errorAbs < self.tolerancia:
            return (str(self.x0) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(self.tolerancia))
        elif dfx == 0:
            return(str(self.x0) + " Es una posible raiz multiple")
        else:
            return("Excedio el numero de iteraciones posible")
