import os
import sys
from flask import *
from flask import render_template
from flask import Flask
from metodos.EcuacionesDeUnaVariable import Plus


app = Flask(__name__)


@app.route('/')  # Decorador o wrap
def index():

    return render_template('index.html')  # Regresa un string


@app.route('/Metodo2', methods=['GET', 'POST'])  # Decorador o wrap
def Metodo2():
    incremento = request.form.get('incremento')
    funcion = request.form.get('funcion')
    valor_inicial = request.form.get('Valor_inicial')
    iteraciones = request.form.get('Iteraciones')

    if request.method == 'POST':
        plus = Plus(incremento, funcion)
        suma = plus.suma()
        print(incremento, funcion, valor_inicial, iteraciones)

    return render_template('busquedasIncrementales.html', suma=suma)


app.run(debug=True)
