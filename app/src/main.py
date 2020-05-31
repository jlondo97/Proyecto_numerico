from flask import *
from flask import render_template
from flask import Flask
from metodos.EcuacionesDeUnaVariable import Plus
from metodos.EcuacionesDeUnaVariable.MetodosPorIntervalos import BusquedasIncrementales

app = Flask(__name__)


@app.route('/')  # Decorador o wrap
def index():

    return render_template('index.html')  # Regresa un string


@app.route('/Metodo1', methods=['GET', 'POST'])  # Decorador o wrap
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


app.run(debug=True)
