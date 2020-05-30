import numpy as np
from sympy import *
import math
functions = []
functionsValues = []
constants = []
constantsUseds = []
a1, a2, a3, a4 = symbols('a1 a2 a3 a4')
b1, b2, b3, b4 = symbols('b1 b2 b3 b4')
c1, c2, c3, c4 = symbols('c1 c2 c3 c4')
d1, d2, d3, d4 = symbols('d1 d2 d3 d4')
e1, e2, e3, e4 = symbols('e1 e2 e3 e4')
f1, f2, f3, f4 = symbols('f1 f2 f3 f4')
g1, g2, g3, g4 = symbols('g1 g2 g3 g4')
h1, h2, h3, h4 = symbols('h1 h2 h3 h4')
i1, i2, i3, i4 = symbols('i1 i2 i3 i4')
j1, j2, j3, j4 = symbols('j1 j2 j3 j4')
k1, k2, k3, k4 = symbols('k1 k2 k3 k4')
l1, l2, l3, l4 = symbols('l1 l2 l3 l4')
m1, m2, m3, m4 = symbols('m1 m2 m3 m4')
n1, n2, n3, n4 = symbols('n1 n2 n3 n4')
constants.append(a1)
constants.append(a2)
constants.append(a3)
constants.append(a4)
constants.append(b1)
constants.append(b2)
constants.append(b3)
constants.append(b4)
constants.append(c1)
constants.append(c2)
constants.append(c3)
constants.append(c4)
constants.append(d1)
constants.append(d2)
constants.append(d3)
constants.append(d4)
constants.append(e1)
constants.append(e2)
constants.append(e3)
constants.append(e4)
constants.append(f1)
constants.append(f2)
constants.append(f3)
constants.append(f4)
constants.append(g1)
constants.append(g2)
constants.append(g3)
constants.append(g4)
constants.append(h1)
constants.append(h2)
constants.append(h3)
constants.append(h4)
constants.append(i1)
constants.append(i2)
constants.append(i3)
constants.append(i4)
constants.append(j1)
constants.append(j2)
constants.append(j3)
constants.append(j4)
constants.append(k1)
constants.append(k2)
constants.append(k3)
constants.append(k4)
constants.append(l1)
constants.append(l2)
constants.append(l3)
constants.append(l4)
constants.append(m1)
constants.append(m2)
constants.append(m3)
constants.append(m4)
constants.append(n1)
constants.append(n2)
constants.append(n3)
constants.append(n4)
f = Function('f') #Defino a 'f' como una funcion
df = Function('df')
x = Symbol('x')
y = Symbol('y')
puntosX = []
putnosY = []
n = 0
puntos = []
puntosDiccionario = {}
intervalos = []
valoresConstantes = {}
def recolectarDatos():
    constanNum = 0
    n = int(input("Ingrese el numero de puntos: "))
    
    for i in range(n):
        puntoActual = str(input("Ingrese los valores de x" +str(i) + ", f(x" + str(i) + ") separados por espacio: "))
        valores = puntoActual.split(" ")
        puntos.append([float(valores[0]),float(valores[1])])
    for i in range(1,n):
        intervalos.append([puntos[i-1][0],puntos[i][0]])
    puntosDiccionario = dict(puntos)
    for i in intervalos:
        f = constants[constanNum]*x**3 +constants[constanNum+1]*x**2 +constants[constanNum+2]*x + constants[constanNum+3] 
        functions.append(f)
        f = constants[constanNum]*x**3 +constants[constanNum+1]*x**2 +constants[constanNum+2]*x + constants[constanNum+3]   - puntosDiccionario[i[0]]
        functionsValues.append(f.subs(x,i[0]))
        f = constants[constanNum]*x**3 +constants[constanNum+1]*x**2 +constants[constanNum+2]*x + constants[constanNum+3]   - puntosDiccionario[i[1]]
        functionsValues.append(f.subs(x,i[1])) 
        constantsUseds.append(constants[constanNum])
        constantsUseds.append(constants[constanNum+1])
        constantsUseds.append(constants[constanNum+2])
        constantsUseds.append(constants[constanNum+3])
        constanNum += 4  
    for i in range(0,len(functions)-1,1):
        f = diff(functions[i],x).subs(x,intervalos[i][1]) - diff(functions[i+1],x).subs(x,intervalos[i+1][0])
        functionsValues.append(f)
    for i in range(0,len(functions)-1,1):
        f = diff(functions[i],x,2).subs(x,intervalos[i][1]) - diff(functions[i+1],x,2).subs(x,intervalos[i+1][0])
        functionsValues.append(f)
    functionsValues.append(diff(functions[0],x,2).subs(x,intervalos[0][0]))
    functionsValues.append(diff(functions[len(functions)-1],x,2).subs(x,intervalos[len(intervalos)-1][1]))
    for i in range(0,len(functionsValues)):
        print(str(i + 1)+") " +str(functionsValues[i]))
    solucion = solve(functionsValues, constantsUseds)
    valoresConstantes = dict(solucion)
    marcador = 0
    funcActual = 0
    valoresDeACuatro = []
    for i in valoresConstantes:
        marcador += 1
        valoresDeACuatro.append(valoresConstantes[i])
        if marcador%4 == 0:
            
            functions[funcActual] = functions[funcActual].subs(constantsUseds[marcador-1],valoresDeACuatro[3])
            functions[funcActual] = functions[funcActual].subs(constantsUseds[marcador-2],valoresDeACuatro[2])
            functions[funcActual] = functions[funcActual].subs(constantsUseds[marcador-3],valoresDeACuatro[1])
            functions[funcActual] = functions[funcActual].subs(constantsUseds[marcador-4],valoresDeACuatro[0])
            print(str(functions[funcActual]) + "             " + str(intervalos[funcActual][0]) + " <=  X <= " + str(intervalos[funcActual][1]))
            valoresDeACuatro = []
            funcActual += 1
recolectarDatos()
