from flask import *
from flask import render_template
from flask import Flask
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import BusquedasIncrementales
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import MetodoBiseccion
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import ReglaFalsa
from metodos.EcuacionesDeUnaVariable.MetodosAbiertos import PuntoFijo
from metodos.EcuacionesDeUnaVariable.MetodosAbiertos import MetodoSecante
#from metodos.EcuacionesDeUnaVariable.MetodosAbiertos import MetodoNewton
from metodos.EcuacionesDeUnaVariable.MetodosAbiertos import MetodoRaicesMultiples
app = Flask(__name__)


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
    extremo_inferior = request.form.get('ei')
    funcion = request.form.get('funcion')
    extremo_superior = request.form.get('es')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteracion')
    resultado = ""

    if request.method == 'POST':
        #print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        metodoBiseccion = MetodoBiseccion(
            extremo_inferior, extremo_superior, tolerancia, iteraciones, funcion)
        resultado = metodoBiseccion.metodoBiseccion()

    return render_template('biseccion.html', resultado=resultado)

# -Metodo de Regla falsa renderizando y procesando valores


@app.route('/regla_falsa', methods=['GET', 'POST'])  # Decorador o wrap
def reglaFalsa_rout():
    extremo_inferior = request.form.get('ei')
    funcion = request.form.get('funcion')
    extremo_superior = request.form.get('es')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteracion')
    resultado = ""

    if request.method == 'POST':
        reglafalsa = ReglaFalsa(
            extremo_inferior, extremo_superior, tolerancia, iteraciones, funcion)
        resultado = reglafalsa.metodoReglaFalsa()

    return render_template('reglaFalsa.html', resultado=resultado)

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

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        puntoFijos = PuntoFijo(xa, tolerancia, iteraciones, f, g)
        resultado = puntoFijos.metodoPuntoFijo()
    return render_template('puntoFijo.html', resultado=resultado)

# Metodo de la secante
@app.route('/secante', methods=['GET', 'POST'])  # Decorador o wrap
def secante_rout():
    x0 = request.form.get('x0')
    f = request.form.get('f')
    x1 = request.form.get('x1')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteraciones')
    resultado = ""

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        secante = MetodoSecante(x0, x1, tolerancia, iteraciones, f)
        resultado = secante.metodoSecante()

    return render_template('secante.html', resultado=resultado)


# metodo de raices multiples
@app.route('/raicesMultiples', methods=['GET', 'POST'])  # Decorador o wrap
def raicesMultiples_rout():
    x0 = request.form.get('x0')
    f = request.form.get('f')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteraciones')
    resultado = ""

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        raicesMultiples = MetodoRaicesMultiples(x0, tolerancia, iteraciones, f)
        resultado = raicesMultiples.metodoRaicesMultiples()

    return render_template('raicesMultiples.html', resultado=resultado)


# metodo Newton


@app.route('/eliminacion_gaussiana', methods=['GET', 'POST'])
def eliminacion_gaussiana_rout():
    return render_template('eliminacionGaussiana.html')


app.run(debug=True)
