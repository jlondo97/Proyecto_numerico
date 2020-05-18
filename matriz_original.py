import numpy as np
from random import random


class matriz_solucion():

    rows = 10
    columns = 10
    nombre = "Matriz solución"

    def llenado_matrix(self):

        llenado = np.random.randint(-5, 5, size=(self.columns, self.rows))
        print("-------------------------------------------------------------")
        print(self.nombre)
        print(llenado)
        print("-------------------------------------------------------------")
        return llenado


class matrizA(matriz_solucion):

    rows = 10
    columns = 10
    nombre = "Matriz A"


class matrizB():

    def multiplicacionAX(self):
        matrizSolucion = matriz_solucion()
        mimatrizA = matrizA()

        b = matrizSolucion.llenado_matrix() * mimatrizA.llenado_matrix()
        return b


prueba = matrizB()
p = prueba.multiplicacionAX()
print("Matriz B \n", p)
