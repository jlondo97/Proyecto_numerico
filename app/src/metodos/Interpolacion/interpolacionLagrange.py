import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

class InterpolacionLagrange:

    def __init__(self, n, x, y):

            self.n = n
            self.x = x
            self.y = y

    def lagrange(self):
        self.n = int(self.n)
        polinomio = ""
        F = Function('F')
        G = Function('G')
        print("\n----------------------------FORMA ESQUEMATICA POLINOMIO DE LAGRANGE---------------------------\n\n----------------- P(X) = L0(X)F(X0) + L1(X)F(X1) + L2(X)F(X2) + ... + LN(X)F(XN)---------------")
        for i in range(self.n):
            L = "("
            for j in range(self.n):
                if (j != i):
                    L += "(x - " + str(self.x[j]) + ")"
            L += ")"
            L += " / ("
            for j in range(self.n):
                if (j != i):
                    L += "(" + str(self.x[i]) + " - " + str(self.x[j]) + ")"

            L += ")"
            L = L.replace(")(",")*(")
            F = parse_expr(L)
            print("\n L" + str(i) + "(x) = " + L.replace("((","(").replace("))",")") + " = " + str(expand(F)))
            if i == self.n-1:
                polinomio += "(" + str(expand(F)) + ")*" + str(self.y[i])
            else:
                polinomio += "(" + str(expand(F)) + ")*" + str(self.y[i]) + " + "

        G = ("P(x) =" +  str(expand(polinomio)))
        print("\n-----------------------------------POLINOMIO INTERPOLANTE DE LAGRANGE --------------------------------\n \n" + "P(X) = " + str(G))
        return G

       


