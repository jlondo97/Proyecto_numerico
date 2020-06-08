import numpy as np
from sympy import *
import math

class SplineLineal:

    def __init__(self, n, x, y):

            self.n = n
            self.x = x
            self.y = y

    def metodoInterpolacionSplineLineal(self):
        self.n = int(self.n)
        respuesta = []
        for i in range(1,self.n):
            pendiente = (self.y[i] - self.y[i-1])/(self.x[i] - self.x[i-1])
            resultado = (pendiente * -self.x[i]) + self.y[i]
            respuesta.append("P(X" + str(i) + ") = " + str(pendiente) + "X + " + str(resultado) + "        " + str(self.x[i-1]) + " <= X <= " + str(self.x[i]))
        return respuesta

