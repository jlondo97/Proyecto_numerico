
from flask import Flask
from flask import render_template
from flask import *


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
        suma = Suma(incremento, funcion)
        print(incremento, funcion, valor_inicial, iteraciones)

    return render_template('busquedasIncrementales.html', suma=suma)


def Suma(a, b):
    suma = int(a) + int(b)
    return str(suma)


app.run(debug=True)  # Se encarga de ejecutar el servidor
