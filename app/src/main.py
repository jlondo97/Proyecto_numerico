from flask import *
from flask import render_template
from flask import Flask, make_response, jsonify
import numpy as np
import json
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import BusquedasIncrementales
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import MetodoBiseccion
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import ReglaFalsa
from metodos.EcuacionesDeUnaVariable.MetodosAbiertos import PuntoFijo
from metodos.EcuacionesDeUnaVariable.MetodosAbiertos import MetodoSecante
from metodos.EcuacionesDeUnaVariable.MetodosAbiertos import MetodoNewton
from metodos.EcuacionesDeUnaVariable.MetodosAbiertos import MetodoRaicesMultiples
from metodos.SistemasDeEcuaciones.MetodosDeEliminacion import EliminacionGaussianaSimple
from metodos.SistemasDeEcuaciones.MetodosDeEliminacion import EliminacionGaussianaPivoteoParcial
from metodos.SistemasDeEcuaciones.MetodosDeEliminacion import EliminacionGaussianaPivoteoTotal
from metodos.SistemasDeEcuaciones.MetodosDeFactorizacionDirecta import Dolittle
from metodos.SistemasDeEcuaciones.MetodosDeFactorizacionDirecta import Croult
from metodos.SistemasDeEcuaciones.MetodosDeFactorizacionDirecta import Cholesky
from metodos.SistemasDeEcuaciones.MetodosIterativos import MetodoJacobi
from metodos.SistemasDeEcuaciones.MetodosIterativos import MetodoGaussSeidel
from metodos.Interpolacion.interpolacionNewtonDiferenciasDivididas import InterpolacionNewton
from metodos.Interpolacion.interpolacionLagrange import InterpolacionLagrange
from metodos.Interpolacion.interpolacionSplineLineal import SplineLineal

app = Flask(__name__)
valores = []
label = []


@app.route('/')  # Decorador o wrap
def index():

    return render_template('index.html')  # Regresa un string

# -------------------------------------------Ecuaciones no lineales , metodos por intervalos -------------------

# Metodo busquedas incrementales accediendo y llamando el metodo incremeto para ser renderizado
@app.route('/busquedas_incrementales', methods=['GET', 'POST'])
def busquedasIncrementales_rout():
    incremento = request.form.get('incremento')
    funcion = request.form.get('funcion')
    valor_inicial = request.form.get('Valor_inicial')
    iteraciones = request.form.get('Iteraciones')
    resultado = ""

    if request.method == 'POST':

        busquedasIncrementales = BusquedasIncrementales(
            funcion, valor_inicial, incremento, iteraciones)
        resultado = busquedasIncrementales.busquedasIncrementales()

    return render_template('busquedasIncrementales.html', resultado=resultado)


# -------------Metodo de biseccion accediendo a valores del front y renderizando ----------
@app.route('/biseccion', methods=['GET', 'POST'])  # Decorador o wrap
def metodoBiseccion_rout():
    global valores
    global label
    extremo_inferior = request.form.get('ei')
    funcion = request.form.get('funcion')
    extremo_superior = request.form.get('es')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteracion')
    resultado = ""
    tabla = ""

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        metodoBiseccion = MetodoBiseccion(
            extremo_inferior, extremo_superior, tolerancia, iteraciones, funcion)
        resultado = metodoBiseccion.metodoBiseccion()
        tabla = metodoBiseccion.vector
        valores = metodoBiseccion.valores
        label = metodoBiseccion.labels

    return render_template('biseccion.html', resultado=resultado, tabla=tabla)


@app.route('/get_data_Biseccion')
def get_data_Biseccion():
    global valores
    global label
    labels = label
    data = valores
    return make_response(jsonify({'payload': json.dumps({'data': data, 'labels': labels})}))


# -Metodo de Regla falsa renderizando y procesando valores


@app.route('/regla_falsa', methods=['GET', 'POST'])  # Decorador o wrap
def reglaFalsa_rout():
    extremo_inferior = request.form.get('ei')
    funcion = request.form.get('funcion')
    extremo_superior = request.form.get('es')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteracion')
    resultado = ""
    tabla = ""

    if request.method == 'POST':
        reglafalsa = ReglaFalsa(
            extremo_inferior, extremo_superior, tolerancia, iteraciones, funcion)
        tabla = reglafalsa.vector
        resultado = reglafalsa.metodoReglaFalsa()

    return render_template('reglaFalsa.html', resultado=resultado, tabla=tabla)

# -----------------------------------Metodos Abiertos --------------------------------------------

# Metodo de punto fijo , renderizando y procesando valores
@app.route('/puntofijo', methods=['GET', 'POST'])  # Decorador o wrap
def puntoFijo_rout():
    xa = request.form.get('xa')
    f = request.form.get('f')
    g = request.form.get('g')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteraciones')
    resultado = ""
    tabla = []

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        puntoFijos = PuntoFijo(xa, tolerancia, iteraciones, f, g)
        resultado = puntoFijos.metodoPuntoFijo()
        tabla = puntoFijos.vector
    return render_template('puntoFijo.html', resultado=resultado, tabla=tabla)

# Metodo de la secante
@app.route('/secante', methods=['GET', 'POST'])  # Decorador o wrap
def secante_rout():
    x0 = request.form.get('x0')
    f = request.form.get('f')
    x1 = request.form.get('x1')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteraciones')
    resultado = ""
    tabla = []

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        secante = MetodoSecante(x0, x1, tolerancia, iteraciones, f)
        resultado = secante.metodoSecante()
        tabla = secante.vector

    return render_template('secante.html', resultado=resultado, tabla=tabla)


# metodo de raices multiples
@app.route('/raicesMultiples', methods=['GET', 'POST'])  # Decorador o wrap
def raicesMultiples_rout():
    x0 = request.form.get('x0')
    f = request.form.get('f')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteraciones')
    resultado = ""
    tabla = []

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        raicesMultiples = MetodoRaicesMultiples(x0, tolerancia, iteraciones, f)
        resultado = raicesMultiples.metodoRaicesMultiples()
        tabla = raicesMultiples.vector

    return render_template('raicesMultiples.html', resultado=resultado, tabla=tabla)


# metodo Newton
@app.route('/metodoNewton', methods=['GET', 'POST'])  # Decorador o wrap
def metodoNewton_rout():
    x0 = request.form.get('x0')
    f = request.form.get('f')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteraciones')
    resultado = ""
    tabla = []

    if request.method == 'POST':
        # print(x0, f, tolerancia, iteraciones)
        metodonewton = MetodoNewton(x0, tolerancia, iteraciones, f)
        resultado = metodonewton.metodoNewton()
        tabla = metodonewton.vector

    return render_template('newton.html', resultado=resultado, tabla=tabla)


# ------------------------- Sistemas de ecuaciones ----------

# Eliminacion gaussina simple
@app.route('/eliminacion_gaussiana', methods=['GET', 'POST'])
def eliminacion_gaussiana_rout():
    objetivos = []
    matrices = []
    
    multiplicadores = []
    n = request.form.get('n')
    if str(n) == "None":
        n = 0
    matriz = np.zeros([int(n), int(n)+1])
    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            matriz[i, j] = float(valor)
    resultado = ""
    if request.method == "POST":

        gaussSimple = EliminacionGaussianaSimple(n, matriz)
        resultado = gaussSimple.eliminacionGaussianaSimple()
        objetivos = gaussSimple.objetivos
        matrices = gaussSimple.matrices
        multiplicadores = gaussSimple.multiplicadores   
       
        for i in range(0,int(n)):
         matrices[i] = np.array(matrices[i].split(','))
         
        print(matrices[0])


    return render_template('eliminacionGaussiana.html', n=int(n), resultado=resultado, objetivos = objetivos, matrices = matrices, multiplicadores = multiplicadores)

# Eliminacion gaussina pivoteo parcial----------------#
@app.route('/pivoteoParcial', methods=['GET', 'POST'])
def pivoteo_parcial_rout():
    n = request.form.get('n')
    if str(n) == "None":
        n = 0
    matriz = np.zeros([int(n), int(n)+1])
    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            matriz[i, j] = float(valor)
    resultado = ""
    if request.method == "POST":
        gaussParcial = EliminacionGaussianaPivoteoParcial(n, matriz)
        resultado = gaussParcial.eliminacionGaussianaPivoteoParcial()

    return render_template('pivoteoParcial.html', n=int(n), resultado=resultado)

#---- eliminacion gaussiana pivoteo total ----#
@app.route('/pivoteoTotal', methods=['GET', 'POST'])
def pivoteo_total_rout():

    n = request.form.get('n')
    if str(n) == "None":
        n = 0
    matriz = np.zeros([int(n), int(n)+1])
    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            matriz[i, j] = float(valor)
    resultado = ""
    if request.method == "POST":
        gaussTotal = EliminacionGaussianaPivoteoTotal(n, matriz)
        resultado = gaussTotal.eliminacionGaussianaPivoteoTotal()

    return render_template('pivoteoTotal.html', n=int(n), resultado=resultado)


@app.route('/Dolittle', methods=['GET', 'POST'])
def Dolittle_rout():

    n = request.form.get('n')
    if str(n) == "None":
        n = 0
    matriz = np.zeros([int(n), int(n)])
    B = []  # vector terminos independientes

    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            if j == int(n):
                B.append(float(valor))
            else:
                matriz[i, j] = float(valor)

    resultado = ""
    if request.method == "POST":
        print(matriz)
        print(B)
        metodoDol = Dolittle(n, matriz, B)
        resultado = metodoDol.dolittle()
    print(resultado)

    return render_template('factorizacionDolittle.html', n=int(n), resultado=resultado)


@app.route('/Croult', methods=['GET', 'POST'])
def Croult_rout():

    n = request.form.get('n')
    if str(n) == "None":
        n = 0
    matriz = np.zeros([int(n), int(n)])
    B = []  # vector terminos independientes

    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            if j == int(n):
                B.append(float(valor))
            else:
                matriz[i, j] = float(valor)

    resultado = ""
    if request.method == "POST":
        print(matriz)
        print(B)
        metodoCroult = Croult(n, matriz, B)
        resultado = metodoCroult.croult()
    print(resultado)

    return render_template('factorizacionCrout.html', n=int(n), resultado=resultado)


@app.route('/cholesky', methods=['GET', 'POST'])
def cholesky_rout():
    n = request.form.get('n')
    if str(n) == "None":
        n = 0
    matriz = np.zeros([int(n), int(n)])
    B = []  # vector terminos independientes

    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            if j == int(n):
                B.append(float(valor))
            else:
                matriz[i, j] = float(valor)

    resultado = ""
    if request.method == "POST":
        print(matriz)
        print(B)
        metodoCholesky = Cholesky(n, matriz, B)
        resultado = metodoCholesky.cholesky()
    print(resultado)

    return render_template('Cholesky.html', n=int(n), resultado=resultado)

# Métodos Iterativos----------------#

# Jacobi
@app.route('/jacobi', methods=['GET', 'POST'])
def jacobi_rout():
    tolerancia = request.form.get('tolerancia')
    niter = request.form.get('iteracion')
    n = request.form.get('n')
    tabla = []
    x = []
    if str(n) == "None":
        n = 0
    matriz = np.zeros([int(n), int(n)])
    B = []  # vector terminos independientes

    for i in range(0, int(n)):
        nombre = "x" + str(i+1)
        valor = request.form.get(nombre)
        x.append(float(valor))

    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            if j == int(n):
                B.append(float(valor))
            else:
                matriz[i, j] = float(valor)

    resultado = ""
    if request.method == "POST":
        jacobi = MetodoJacobi(n, matriz, B, x, niter, tolerancia)
        resultado = jacobi.metodoJacobi()
        tabla = jacobi.vector

    # cambiar plantilla de jacobi  y cambiar abajo la direccion a esa plantilla
    return render_template('jacobi.html', n=int(n), resultado=resultado, tabla=tabla)

# --------Gauss seidel
@app.route('/gaussSeidel', methods=['GET', 'POST'])
def GaussSeidel_rout():
    tolerancia = request.form.get('tolerancia')
    niter = request.form.get('iteracion')
    n = request.form.get('n')
    tabla = []

    x = []

    if str(n) == "None":
        n = 0
    matriz = np.zeros([int(n), int(n)])

    B = []  # vector terminos independientes

    for i in range(0, int(n)):
        nombre = "x" + str(i+1)
        valor = request.form.get(nombre)
        x.append(float(valor))

    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            if j == int(n):
                B.append(float(valor))
            else:
                matriz[i, j] = float(valor)

    resultado = ""
    if request.method == "POST":

        if tolerancia == "None":
            tolerancia = 0.00005

        gaussSed = MetodoGaussSeidel(n, matriz, B, x, niter, tolerancia)
        resultado = gaussSed.metodoGaussSeidel()
        tabla = gaussSed.vector

    # cambiar plantilla de gauss y cambiar abajo la direccion a esa plantilla
    return render_template('gaussSeidel.html', n=int(n), resultado=resultado, tabla=tabla)


# Interpolacion----------------#

@app.route('/newtonConDiferenciasDivididas', methods=['GET', 'POST'])
def newton_diferencias_divididas_rout():
    n = request.form.get('n')
    if str(n) == "None":
        n = 0
    tabla = np.zeros([int(n), int(n)+1])

    for i in range(0, int(n)):
        for j in range(0, int(n)+1):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)

            if valor == None:
                valor = 0
            tabla[i, j] = float(valor)

    resultado = ""
    if request.method == "POST":
        print(tabla)
        interNewton = InterpolacionNewton(n, tabla)
        resultado = interNewton.Newton()
    print(resultado)

    return render_template('newtonConDiferenciasDivididas.html', resultado=resultado)


@app.route('/lagrange', methods=['GET', 'POST'])
def lagrange_rout():
    n = request.form.get('n')
    proceso = []
    if str(n) == "None":
        n = 0
    X = []
    Y = []
    for i in range(0, int(n)):
        for j in range(0, int(2)):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            if j == 0:
                X.append(float(valor))
            else:
                Y.append(float(valor))
    resultado = ""
    print(X)
    print(Y)
    if request.method == "POST":
        interLagr = InterpolacionLagrange(n, X, Y)
        resultado = interLagr.lagrange()
        proceso = interLagr.proceso
    print(resultado)

    return render_template('interpolacionLagrange.html', resultado=resultado, proceso = proceso, n = int(n))

@app.route('/splineLineal', methods=['GET', 'POST'])
def spline_lineal_rout():
    n = request.form.get('n')
    if str(n) == "None":
        n = 0
    X = []
    Y = []
    for i in range(0, int(n)):
        for j in range(0, int(2)):
            nombre = str(i+1) + "-" + str(j+1)
            valor = request.form.get(nombre)
            if j == 0:
                X.append(float(valor))
            else:
                Y.append(float(valor))
    resultado = ""
    print(X)
    print(Y)
    if request.method == "POST":
        splinelineal = SplineLineal(n, X, Y)
        resultado = splinelineal.metodoInterpolacionSplineLineal()
    print(resultado)
    return render_template('interpolacionSplineLineal.html', n = int(n), resultado=resultado)


@app.route('/splineCuadratico', methods=['GET', 'POST'])
def spline_cuadrático_rout():

    return render_template('interpolacionSplineCuadratico.html')


@app.route('/splineCubico', methods=['GET', 'POST'])
def spline_cubico_rout():

    return render_template('interpolacionSplineCubico.html')


@app.route('/index', methods=['GET', 'POST'])
def index_rout():

    return render_template('index.html')

app.run(debug= True) 
