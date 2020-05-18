
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')  # Decorador o wrap
def index():

    return render_template('index.html')  # Regresa un string


@app.route('/2')  # Decorador o wrap
def Metodo2():
    return 'Hello, people'  # Regresa un string


app.run(debug=False, port=8000)  # Se encarga de ejecutar el servidor
