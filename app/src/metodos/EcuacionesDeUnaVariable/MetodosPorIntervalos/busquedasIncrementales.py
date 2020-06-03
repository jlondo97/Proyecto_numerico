from __future__ import division
from sympy import *
from sympy.parsing.sympy_parser import parse_expr


class BusquedasIncrementales:
    f = Function('fx')

    def __init__(self, funcion, x0, delta, iteraciones):

        self.funcion = funcion
        self.x0 = x0
        self.delta = delta
        self.iteracion = iteraciones

    def busquedasIncrementales(self):
                
        self.x0 = float(self.x0) 
        self.delta = float(self.delta)
        self.iteracion = float(self.iteracion)
        
        f = parse_expr(self.funcion)
        x = Symbol('x')
        fx0 = f.subs(x, self.x0)
        if fx0 == 0:
            mensaje = (str(self.x0) + " es una raiz")
            return mensaje

        else:
            x1 = self.x0 + self.delta
            cont = 1
            fx1 = f.subs(x, x1)
            while fx0*fx1 > 0 and cont < self.iteracion:
                self.x0 = x1
                fx0 = fx1
                x1 = self.x0 + self.delta
                fx1 = f.subs(x, x1)
                cont = cont + 1

            if fx1 == 0:
                mensaje = (str(x1) + " es una raiz")
                return mensaje
            elif fx0 * fx1 < 0:
                mensaje = ("Hay una raiz entre: " +
                           str(self.x0) + " and " + str(x1))
                return mensaje
            else:
                mensaje = ("Excedio el numero de iteraciones posible")
