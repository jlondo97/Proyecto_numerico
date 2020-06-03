from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


class MetodoRaicesMultiples:
    f = Function('fx')
    df = Function('dfx')
    d2f = Function('d2fx')

    def __init__(self, x0, tolerancia, iteraciones, f):  
        self.x0 = x0
        self.iteraciones = iteraciones
        self.tolerancia = tolerancia
        self.f = f
       

    def metodoRaicesMultiples(self):
        self.x0 = float(self.x0)
        self.tolerancia = float(self.tolerancia)
        self.iteraciones = float(self.iteraciones)

        f = parse_expr(self.f)

        x = Symbol('x')
        df = diff(f,x)
        d2f = diff(df,x)
        fx = f.subs(x,self.x0)
        dfx = df.subs(x,self.x0)
        d2fx = d2f.subs(x,self.x0)
        cont = 0
        errorAbs = self.tolerancia + 1
        denominador = dfx**2 - (fx*d2fx)
        
        while fx != 0 and errorAbs > self.tolerancia and denominador != 0 and cont < self.iteraciones:
            x1 = self.x0 - fx*dfx/(dfx**2 - (fx*d2fx))
            fx = f.subs(x,x1)
            dfx = df.subs(x,x1)
            d2fx = d2f.subs(x,x1)
            errorAbs = abs(x1 - self.x0)
           #errorRel = errorAbs/x1
            self.x0 = x1
            cont += 1
        

        if fx == 0:
            mensaje = (str(self.x0) + " es una raiz")
            return mensaje
        elif errorAbs < self.tolerancia:
            mensaje = (str(self.x0) + " se aproxima a una raiz de la función, con una tolerancia de: " + str(self.tolerancia))
            return mensaje
        elif dfx == 0:
            mensaje = (str(self.x0) + " Es una raiz multiple simple")
            return
        elif d2fx == 0:
            mensaje = (str(self.x0) + " Es una raiz multiple de multiplicidad 2")
            return mensaje
        else:
            mensaje = ("Excedio el numero de iteraciones posible")
            return mensaje

    
