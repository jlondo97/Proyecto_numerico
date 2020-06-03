from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr



class MetodoSecante:
    f = Function('fx')
    def __init__(self, x0, x1, tolerancia, iteraciones, f):  
        self.x0 = x0
        self.x1 = x1
        self.iteraciones = iteraciones
        self.tolerancia = tolerancia
        self.f = f
        
    def metodoSecante(self):
        self.x0 = float(self.x0)
        self.x1 = float(self.x1)
        self.tolerancia = float(self.tolerancia)
        self.iteraciones = float(self.iteraciones)

        f = parse_expr(self.f)
        x = Symbol('x')
        fx0 = f.subs(x,self.x0)
        if fx0 == 0:
            mensaje = (str(self.x0) + " es una raiz")
            return mensaje
        else:
            fx1 = f.subs(x,self.x1)
            cont = 0
            errorAbs = self.tolerancia + 1
            denominador = fx1 - fx0
            while fx1 != 0 and errorAbs > self.tolerancia and denominador != 0 and cont < self.iteraciones:
                x2 = self.x1 - fx1*(self.x1-self.x0)/denominador
                errorAbs = abs(x2 - self.x1)
                #errorRel = errorAbs/x2
                self.x0 = self.x1
                fx0 = fx1
                self.x1 = x2
                fx1 = f.subs(x,self.x1)
                denominador = fx1 - fx0
                cont += 1


            if fx1 == 0:
                mensaje = (str(self.x1) + " es una raiz")
                return mensaje
            elif errorAbs < self.tolerancia:
                mensaje = (str(self.x1) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(self.tolerancia))
                return mensaje
            elif denominador == 0:
                mensaje = ("Hay una raiz multiple en " + str(self.x1))
                return mensaje
            else:
                mensaje = ("Excedio el numero de iteraciones posible")
                return mensaje

