import numpy as np
from random import random


class matriz_solucion():

    rows = int(input("Enter a matrix size: "))
    sigma = int(input("Define a sigma number: "))
    columns = rows
    nombre = "Matriz solución"

    def llenado_matrix(self):

        llenado = np.random.randint(-1000, 1000,
                                    size=(self.columns, self.rows))
        llenado = diagonalReplace(llenado, self.sigma)
        print("-------------------------------------------------------------")
        print(self.nombre)
        print(llenado)
        print("-------------------------------------------------------------")
        return llenado


class matrizA(matriz_solucion):

    nombre = "Matriz A"


class matrizB():

    def multiplicacionAX(self):
        matrizSolucion = matriz_solucion()
        mimatrizA = matrizA()

        b = matrizSolucion.llenado_matrix() * mimatrizA.llenado_matrix()
        return b


def diagonalReplace(matriz, sigma):
    for i in range(len(matriz)):
        value = 0
        for j in range(len(matriz[i])):
            valueToAdd = abs(matriz[i][j])
            value += valueToAdd
        matriz[i][i] = value + sigma
    return matriz


prueba = matrizB()
p = prueba.multiplicacionAX()
print("Matriz B \n", p)
