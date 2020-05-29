import numpy as np

print("Factorizadcion LU")

m = int(input("Numero de columnas :"))
matriz = np.zeros([m, m])
u = np.zeros([m, m])
L = np.zeros([m, m])

print("introduce los elementos de la matriz: ")

for r in range(0, m):
    for c in range(0, m):
        matriz[r, c] = input("Elemento a["+str(r+1)+","+(str(c+1)+"] = "))
        matriz[r, c] = float(matriz[r, c])
        u[r, c] = matriz[r, c]
 # operaciones para hacer  ceros debajo de la diagonal principal
for k in range(0, m):
    for r in range(0, m):
        if (k == r):
            L[k, r] = 1
        if (k < r):
            factor = (matriz[r, k]/matriz[k, k])
            L[r, k] = factor
            for c in range(0, m):
                matriz[r, c] = matriz[r, c] - (factor * matriz[k, c])
                u[r, c] = matriz[r, c]

print("impresion de resultados")
print("Matriz L")
print(L)
print("Matriz u")
print(u)
print("comprobacion")
a = np.dot(L, u)
print(a)
