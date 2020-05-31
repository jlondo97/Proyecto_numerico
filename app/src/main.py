from flask import *
from flask import render_template
from flask import Flask
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import BusquedasIncrementales
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import MetodoBiseccion
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import ReglaFalsa

app = Flask(__name__)


@app.route('/')  # Decorador o wrap
def index():

    return render_template('index.html')  # Regresa un string


# Decorador o wrap
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


@app.route('/biseccion', methods=['GET', 'POST'])  # Decorador o wrap
def metodoBiseccion_rout():
    extremo_inferior = request.form.get('ei')
    funcion = request.form.get('funcion')
    extremo_superior = request.form.get('es')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteracion')
    resultado = ""

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        metodoBiseccion = MetodoBiseccion(
            extremo_inferior, extremo_superior, tolerancia, iteraciones, funcion)
        resultado = metodoBiseccion.metodoBiseccion()

    return render_template('biseccion.html', resultado=resultado)


@app.route('/regla_falsa', methods=['GET', 'POST'])  # Decorador o wrap
def reglaFalsa_rout():
    extremo_inferior = request.form.get('ei')
    funcion = request.form.get('funcion')
    extremo_superior = request.form.get('es')
    tolerancia = request.form.get('tolerancia')
    iteraciones = request.form.get('iteracion')
    resultado = ""

    if request.method == 'POST':
        # print(funcion, extremo_superior,extremo_inferior,tolerancia,iteraciones)
        reglafalsa = ReglaFalsa(
            extremo_inferior, extremo_superior, tolerancia, iteraciones, funcion)
        resultado = reglafalsa.metodoReglaFalsa()

    return render_template('reglaFalsa.html', resultado=resultado)


app.run(debug=True)
