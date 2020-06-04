from numpy import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import math

class InterpolacionNewton:

    def __init__(self, n, tabla):

            self.n = n
            self.tabla = tabla

    def Newton(self):
        self.n = int(self.n)
        polinomio = "P(X) = " + str(self.tabla[0][1])
        F = Function('F')
        for j in range(2,self.n+1):
            for i in range(j-1,self.n):
                self.tabla[i][j] = (self.tabla[i][j-1] - self.tabla[i-1][j-1])/(self.tabla[i][0] - self.tabla[i-j+1][0])
                if(i==j-1):
                    polinomio += " + " + str(self.tabla[i][j])
                    for i in range(0,i):
                        polinomio += "(x - " + str(self.tabla[i][0]) + ")"

        #imprimirTabla(tabla,n)
        F = parse_expr(polinomio.replace("P(X) = ","").replace("(","*("))
        print("\n-----------------------------------POLINOMIO INTERPOLANTE DE NEWTON CON DIFERENCIAS DIVIDIDAS --------------------------------\n \n" + "Forma esquematica: " + polinomio + "\n Forma Simplificada: P(X) = " + str(expand(F)))
        return ("P(X) = " + str(expand(F)))

    # def imprimirTabla(tabla,n):
    #     print(" n |   xi   |      f[xi]     |         primera         |          Segunda          |          Tercera          |         Cuarta         |         Quinta        |Nesima|" )
    #     for i in range(n):
    #         print(str(i) + "     " + str(tabla[i]).replace("'"," ").replace(",","       ").replace("["," ").replace("]"," ").replace(" 0 ", " "))
    #         print("\n")




