import math


def __main__():

    intervalo_a = 0
    intervalo_b = 5
    incremento = 0.1
    Busqueda_inc(intervalo_a, intervalo_b, incremento)


def funcion(a):
    return math.exp(-(a**2)+7)-a*math.log((a**4)+5)-(a**2)+20


def Busqueda_inc(intervalo_a, intervalo_b, incremento):
    Nraices = 0
    if funcion(intervalo_a) == 0:
        Nraices = +1
        tabla = "<{}><{}>".format(intervalo_a, intervalo_a+incremento)
        print("En f(", intervalo_a, ") existe una raiz")

    if (funcion(intervalo_b) == 0):
        Nraices = +1
        tabla = "<{}><{}>".format(intervalo_b, intervalo_b+incremento)
        print("En f(", intervalo_b, " ) existe una raiz")

    else:

        while intervalo_a <= intervalo_b:
            c = intervalo_a + incremento
            if funcion(intervalo_a) * funcion(c) < 0:
                Nraices += 1
                tabla = "<{}><{}>".format(intervalo_a, c)
                intervalo_a = c
            else:
                intervalo_a = c

    if Nraices == 0:
        print("No se encontraron raices en el intervalo \n")

    else:
        print("Se encontraron raices en los siguientes intervalos")
        print(tabla)


if __name__ == "__main__":
    __main__()
